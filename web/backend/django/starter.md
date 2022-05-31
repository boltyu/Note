# simple translate for django tutorial doc
# 创建项目
        django-admin startproject mysite
    mysite/#根文件夹包含工程，名字
    manage.py#与此项工程交互的[命令行工具](manager.md)
    |mysite/#python包名
    |-__init__.py#
    |-settings.py#
    |-urls.py#url[派遣器](urldispatcher.md)
    |-asgi.py#ASGI兼容服务端点
    |-wsgi.py#WSGI兼容服务端点
## 测试运行
        manager.py runserver 80
    切记不要在其它类似的环境中运行服务。django主要提供web框架而不是web服务，[关于runserver](runserver.md)

## 创建一个投票应用
        projects和apps
        应用实现一些特定功能，一个网站的配置与apps的合集叫做project。project可以包含多个apps，一个app可以隶属多个projects
    在工程中创建一个app polls
        manager.py startapp polls
    |polls/#
    |-__init__.py
    |-admin.py
    |-apps.py
    |-migrations/
    |--__init__.py
    |-models.py
    |-tests.py
    |-views.py
## 写第一个视图
        from django.http import HttpResponse
        def index(request):
            return HttpResponse('Hello, world. You\'re at the polls index.')
    此外我们需要此视图的创建url，在polls目录下创建urls.py
        from django.urls import path
        from . import views
        urlpatterns = [
            path('', views.index, name='index'),
        ]
    接着还要为此应用创建url，在mysite目录下修改urls.py，主要使用了django.urls的include方法
        from django.contrib import admin
        from django.urls import include, path
        urlpatterns = [
            path('polls/', include('polls.urls')),
            path('admin/', admin.site.urls),
        ]
    当django遇到include方法时，便会裁掉父目录字符，将剩余的路径字符传给子包进一步处理，还是挺灵活的。admin.site.urls是个例外，不需要用include方法

# 关于path
    path有四个参数，route，view是必须提供的，kwargs和name是可选的
    route是一个含有url样式的字符串。django会在urlpatterns中向下查找目标
    当django在urlpatterns中找到目标后，会将HttpRequest作为首个参数调用目标对应的视图函数。
    kwargs待补充
    name使得你可以仅从单独一个文件中便可作出对url样式的全局更改，待补充

# 数据库安装配置
    默认使用SQLite。要使用其它数据库时，打开mysite/settings.py，在DATABSASES的default字段里填写ENGINE和NAME
        ENGINE
            django.db.backends.sqlite3
            django.db.backends.mysql等等
        NAME
            数据库名称，sqlite中数据库名实为电脑中的一个文件，此时要用绝对路径。如果使用了其他数据库还要添加USER PASSWORD HOST，详见[数据库](databases.md)
        为了确保django可以创建测试数据库，请提供一个有创建数据库权限的USER
    TIME_ZONE顺便还可以把时区设置了
    注意在INSTALLED_APPS中，一些默认激活的app可能至少用到了一张数据表，所以我们有必要在使用之前创建这些表：
        manage.py migrate
    同样当你不需要一些预置app时，只需将他们从INSTALLED_APPS中删除或注释，migrate也不会为他们创建数据表了

# 创建模型
    模型包含了数据库结构，和一些附加的metadata
        django比较推崇DRY原则，dont repeat yourself，将你的数据模型定义在一个地方，然后从他继承数据里的东西。包括迁移，迁移是完全从模型文件中继承而来，本质上就是个变更历史，根据此历史django可为当前模型对症下药更新数据库的schema????
    在我们的poll app中，创建两个模型Question和Choice。Question包含问题和发布时间，Choice包含描述和统计。一个Choice关联一个Question
    在polls/models.py文件中：
        from django.db import models
        class Question(models.Model):
            question_text = models.CharField(max_length=200)
            pub_date = models.DateTimeField('date published')
        class Choice(models.Model):
            question = models.ForeignKey(Question, on_delete=models.CASCADE)
            choice_text = models.CharField(max_length=200)
            votes = models.IntegerField(default=0)
    如上，每个模型由一个django.db.models.Model类来描述，每个模型有一定数量的类，每个类在模型中代表一个数据库表,每个Filed实例的名字也是表的列名，在python中你可以直接用这个名字，并且他也会作为你数据库的列名
    第一个参数是个可选的占位参数Filed=?，如果你没有给定它，那么将使用类变量名，上例中的pub_date便给定了一个人机友好的名字。
    一些Filed类要求提供参数，如CharField要求给定max_length，起到校验数据的功能
    Filed可以有不同的可选参数，比如我们将vote的默认值通过default=设置为0
    最后，使用外键ForeignKey告诉Django单个Choice与单个Question关联。

## 使用模型
    有了模型，Django可以帮助我们创建表，同时创建与这些表交互的api对象。我们马上要做的是激活这个模型
        Djangoapp是可插拔的，可以在多个项目中使用一个app，app可以发布，因为它不会与Django的安装绑定
    为了在项目中包含app，我们需要在settings中INSTALLED_APPS段添加app的项目
        INSTALLED_APPS = [
            'polls.apps.PollsConfig',
            ...]    
    然后做个迁移
        manage.py makemigrations polls
    上面命令告诉Django模型已经更改，需要更新。迁移文件存储在你的硬盘上，如polls/migrations/0001_initial.py，记录着做了哪儿些改变。
        manage.py sqlmigrate polls 0001
    使用上述命令查询具体对SQL做了什么
    表名会使用app名拼接小写的模型名，可重写
    主键IDs会自动添加，可重写
    外键关系由FOREIGN KEY显式的约束，不用担心DEFERRABLE部分？
    sqlmigrate命令实际

## Django管理接口介绍
    创建一个管理员，默认可以使用/admin界面
        manager.py createsupperuser
    为自己的app添加admin接口，只需在admin.py中
        from django.contrib import admin
        from .models import Question
        admin.site.register(Question)
    这样，Django便知道要将你的app模型添加到admin管理中，同时生成与之相对应的表单，不同的模型字段对应不同的html input组件
    添加更多的视图，在polls/views.py中
        def result(request,question_id):
            response = 'result of Question%s'
            return HttpResponse(response % question_id)
    同样要定义url，在polls/urls.py添加与之对应的调用
        urlpatterns = [...
            path('<int:question_id>/results/',view.results,name='results')]
    <int:是一个转换器，决定了将会匹配url的样式，question_id>将会被捕获为关键变量传入视图函数中。详见[url派遣器](urldispatcher.md)

# 编写你的视图
    首先看一个例子：
        def index(request):
            latest_question_list = Question.objects.order_by('-pub_date')[:5]
            output = '.'.join([x.text for x in latest_question_list])
            return HttpResponse(output)
    上述方法首先获取了Question中日期最近的五项，然后把他们的text属性拼接起来作用内容。这样的内容是硬编码的，不容易更改，所以Django要用到模版系统来解决。
    每个视图都要返回一个包含内容的HttpResponse对象，或者引发Http404。通常，一个视图根据参数来获取数据，然后用获取的数据渲染模版：
        render(request,'path to html',render_data)
## 设计你自己的模版
    变量使用{{}}来包含，如:
        {{article.pub_date|date:"F j, Y"}}
    '|'是Unix风格的管道pipe，可以起过滤作用，上例便是对时间进行了格式化。管道数量可以累加。
```
        {\%extend "base.html"%}
```
        是模版继承，它表示首先要加载模版"base.html",在那里面已经定义了一些block，如：
``` 
        {\%block title%} {\%endblock}
```
    我们只需在扩展html中完善实现它的具体内容就行了：
```
        {\%extend "base.html"%}
        {\%bock title%} HELLO {\%endblock%}
```
    这种方式非常灵活，使得你可以任意更改站点版本，只需将子模版（使用extend的html）复用即可。Django的创建者已经使用这种技术来创建各个显著不同的手机版站点，只需创建一个新的base模版就好了。
## 渲染模版的两种方式
    一
        from django.template import loader
        ttt = loader.get_template('path to html')
        data = {...:...}
        return HttpResponses(ttt.render(data,context))
    二
        from django.shortcuts import render
        return render(request,"path to html",context)
    render函数使用request作为第一参数，第二个模版路径，第三个是映射变量用的字典???，render返回一个HttpResponse对象
## 引发404错误
        try:
            ...
        except ObjectDoesNotExistErorr:
            raise Http404("sorry ...")
    相比上句，Django有个更方便的函数：
        get_object_or_404(Question,pk=...)
    当获取模型中对象不存在时自动引发Http404，它用Django模型作为第一参数，然后可以又多个关键字匹配参数。
    我们为什么要用它来代替手动捕获异常？因为这样手动捕获会耦合模型和视图层，而Django最重要的目标之一便是解耦。与此类似的还有get_list_or_404()....
    模版使用'.'来查找访问变量的属性，但在此之前会先已字典方式查找值。
## 移除硬编码的URLs
    一些html中的硬编码的url像这样：
        href = "/polls/{{question_id}}"
    硬编码同样有耦合的问题，在有很多模版的项目中更改url会很困难。然而这也可以通过以下方式缓解：
```
        {\% url 'detail' question_id %}
        path('specifics/<int:question_id>',view.detail,name='detail')
```
    使用模版标签```{\%url%}```来解决对特定url路径依赖的问题，它会自动在urls模块中查找匹配项。模版标签中'detail'将解释为路径'specifics/<int:question_id>'，question_id补充其内容
## 命名空间URL名称
    这个教程仅仅是个app，而在实际Django工程里，会有五个、十个或者更多。Django该如何区分它们的URL名称，比如polls app有一个detail视图，然后同一工程里的另一个blog app也有一个detail视图。当你用```{\%url%}```时django该如何判断是哪个。
    答案就是在URLconf里使用命名空间，在polls/urls.py文件中，在开头添加app_name来设置app的命名空间
        from django.urls import path
        from . import views
        app_name = 'polls'
        urlpatterns = {
            path('',views.index,name='index'),
            ....}
    然后在对你的模版中的url标签做一些改进：
```
         <li><a href="{\% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

## 写一个简单的表单
    请参考 Write a minimal form
    python视图例子：
        from django.http import HttpResponse, HttpResponseRedirect from django.shortcuts import get_object_or_404, render from django.urls import reverse
        from .models import Choice, Question # ...
        def vote(request, question_id):
            question = get_object_or_404(Question, pk=question_id)
            try:
                selected_choice = question.choice_set.get(pk=request.POST['choice']) 
            except (KeyError, Choice.DoesNotExist):
                return render(request, 'polls/detail.html',{'queston':question,'error_message': "You didn't select a choice.",}) 
            else:
                selected_choice.votes += 1
                selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))     
    request.POST是个类似于字典的对象，让你可以通过键名访问POST的对象，并且其值总是string。同样Django提供了request.GET来访问GET的对象。
    我们要在代码中显式地使用request.POST来确保数据仅会在POST方法时更改。和flask一样，如果用户提交过来的键名不存在会引发KeyError。
    例程中使用了HttpResponseRedirect而不是HttpResponse，因为前者使用单个参数：即用户要跳转到的地址。其中的reverse()函数可以避免在视图函数中使用url硬编码。上例中它会返回：
        /polls/3/results/
    在有人对某个问题投票后，vote()视图将会重定向至结果页面，要注意这里模版名字暂时还是硬编码????：
        def results(request, question_id):
            question = get_object_or_404(Question, pk=question_id)
            return render(request, 'polls/results.html', {'question': question})
    此时的vote视图仍有个小问题，就是访问冲突，当两个人同时投票时，计数会出现问题，我们把这种冲突叫做条件竞争，后面会介绍如何避免此情况

# 通用视图系统：代码越少越好
    detail()和results()视图代码都非常精短，这些视图都是具有代表性的基础web开发的例子：根据随url传来的参数去数据库中获得数据，加载一个模版并渲染它，因为这几个功能比较通用，Django提供了快捷的方法---通用视图系统(generic view)。
    为什么要code-shuffle：
        通常写一个Django app，你要考量通用视图是否能解决你的问题，并且最好从一开始就使用通用视图。教程中是为了教学而中途修改。
## 开始修改
    在polls/urls.py中：
        urlpatterns = [
            path('', views.IndexView.as_view(), name='index'),
            path('<int:pk>/', views.DetailView.as_view(),name='detail'), 
            path('<int:pk>/results/', views.ResultsView.as_view(), name='results'), 
            path('<int:question_id>/vote/', views.vote, name='vote')]
    在polls/views.py中：
        from django.http import HttpResponseRedirect
        from django.shortcuts import get_object_or_404, render from django.urls import reverse
        from django.views import generic
        from .models import Choice, Question
        class IndexView(generic.ListView):
            template_name = 'polls/index.html' 
            context_object_name = 'latest_question_list'
            def get_queryset(self):
                """Return the last five published questions."""
                return Question.objects.order_by('-pub_date')[:5]
        class DetailView(generic.DetailView):
            model = Question
            template_name = 'polls/detail.html'
        class ResultsView(generic.DetailView）: 
            model = Question
            template_name = 'polls/results.html'
        def vote(request, question_id):
        ... # same as above, no changes needed.
    上述我们使用了两种通用视图，ListView和DetailView，它们会自动生成模版名字，比如<app name>/<model name>_detail.html。其中template_name变量是告诉Django由我们指定的模版的名字而不是由它自己生成，这样即使同属一个类但外观却可以不同
    在先前例子中模版一般会被提供一个context变量来动态补充其中的内容，对于DetailView则会自动提供question，因为我们为其指定了模型，而ListView会自动生成question_list，所以我们还是用context_object_name为其指定具体名称

# 自动化测试
    测试是检测代码强健性的方式。
    测试操作有多个等级。一些测试
    为什么需要测试
    测试将会节省你的时间
    测试不只是鉴别问题，还能阻止他们
    测试使代码更能被大家接受
    测试帮助团队协作
## 基本测试策略
    一些程序员遵循 测试驱动开发 的准则。他们实际上在写代码前就已经写了测试。也许有些不可思议，但其实和大多数人常做的一样：描述一个问题，创建代码解决它。很难说要从哪儿里开始写测试，但如果你已经写几千行的python，那么测试起来不会容易的。
## 写第一个测试
    
