# 基于类的视图
可将视图结构化，通过继承和Mixin（Multiple Inheritance）来重用代码
# 使用方法
核心目的是，用不同的类实例方法来响应不同的HTTP请求方法，避免在单个函数视图中用条件分支来响应
在函数视图中我们处理一个GET请求可能会这样：
    if request.method == 'GET':
而在基于类视图中
    class MyView(View):
        def get(self,request):
            return HttpResponse('result')
由于Django的url处理器期望把请求及相关变量传给一个可调用函数而不是一个类，所以基于类的视图有个as_view()方法来返回一个可以被调用的函数，这个函数创建类的一个实例，并且调用setup()去初始化它的特性，然后调用它的dispatch()方法，dispatch查看request看是不是GET，POST等，如果都没有就引发HttpResponseNotAllowed
    path('about/',MyView.as_view(),
你的方法返回的东西和你的函数视图返回的东西，是不是一样没有所谓?????这意味着在基于类的视图中http shortcuts和TemplateResponse对象可以使用。
# 类属性
使用python风格来玩转
    class GreetingView(View):
        greeting = "Good Day"

    class MorningGreetingView(GreetingView):
        greeting = "Morning to ya"
试试as_view()
    path('about/',GreetingView.as_view(greeting="G'day")),
# 使用mixins
mixins是多重继承的一种形式，即特性和属性由多个父类继承组合而来。
例如在通用基于类的视图中有个TemplateResponseMixin，它主要定义了render_to_response()方法，当与View类组合时，结果是一个TemplateView类，它会分发请求给合适的方法，而这些方法恰巧由View继承而来，同时它还有render_to_response()方法通过模版名称返回一个模版响应对象（TemplateResponse object）
mixins是通过继承多类来重用代码的绝佳方式，但是会带来更高的功耗，在mixins间你的代码越分散，读取子类就越困难，如果你有个层次较深的继承树那么查找那些被重写的方法时也将耗费更多资源
还要说的是仅能继承一个通用视图，也就是说父类中仅能有一个继承自View，剩余的应该是mixins，如果不这么做，比如同时继承ProcessFormView和ListView，可能结果和预期会有出入
# 处理forms

# 装饰基于类的视图
即使不是函数视图，也可以用装饰器，并且使用as_view()或者创建子类时装饰器工作的方式也不一样。
## 在URLconf中使用装饰器
    path("about/", login_required(TemplateView.as_view(template_name="secret.html"))),
    path("vote/", permission_required('polls.can_vote')(VoteView.as_view())),
## 装饰类
为了装饰每一个基于类的视图的实例，你需要先装饰类定义。做法是在类中的dispatch()方法前使用装饰器。
类中的方法和独立的函数有些不同，所以不能直接将装饰器用在方法上，而是要先将其变为方法装饰器。
    from django.contrib.auth.decorators import login)required
    from django.utils.decorators import method_decorator
    from django.views.generic import TemplateView
    class ProtectedView(TemplateView):
        template_name = "secret.html"
        @method_decorator(login_required)
        def dispatch(self,*args,**kargs):
            return super().dispatch(*args,**kargs)
下面的形式更为简洁
    @method_decorator(login_required, name='dispatch')
    class ProtectView(TemplateView):
        template_name = 'secret.html'
下面的形式针对多项装饰器
    decorators = [never_cache,login_required]
    @method_decorator(decorators, name='dispatch')
    class ProtectedView(TemplateView):
        template_name = 'secret.html'
在以上例子中，每个ProtectView的实例都将具有登录保护，这些例子都使用了login_required，不过同样的效果也可以通过LoginRequiredMixin来实现。
    注意，method_decorator传入了*args和**kwargs，你的方法如果没有兼容这些传入参数，那么会引发TypeError异常

# 内建基于类的通用视图
如果我们重复的写样式什么的，那么网络开发就很单调。Django尝试从模版和模型两个方面着手改进的这些问题，视图层如何呢？
我们可以归类一些共同的任务，比如显示包含有对象的列表。
## 对象的通用视图
模版视图TemplateView肯定是有用的，但是django的通用视图在处理你的数据库内容上会更放光彩。
我们可以显式的添加一个template_name属性来告诉视图用哪儿个模版。如果没有显式添加，则django根据对象名称推断一个。比如"books/publisher_list.html"，其中books来自模型中app的名字，publisher是模型名称的小写形式。
    因此，在TEMPLATES中的DjangoTemplates后端的APP_DIR选项设置为True时,模版的位置会是/path/to/project/books/templates/books/publisher_list.html 
## 让模版context名称友好化

