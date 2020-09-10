# 处理用户request的流程
    1.确定root url所在模块，默认配置在ROOT_URLCONF中，也可能随HttpRequest对象传入
    2.加载url模块并寻找urlpatterns，它是由path()及re_path()实现的序列
    3.遍历每个path，寻找匹配目标
    4.成功匹配后调用相关视图函数或基于view的视图类，调用过程同时传入HttpResponse实例，匹配的url可能包含表达式、关键字参数、未命名组？
    5.匹配失败或者出现了异常，会调用一个错误视图来处理
    几个例子：
        path('articles/2003/',views.x)
        path('articels/<int:year>/',views.xx)
        path('articels/<int:year>/<int:month>/',views.xxx)
        path('articels/<int:year>/<int:month>/<slug:slug>/',views.xxxx)
    上例可以看出，使用尖括号来匹配url中的参数，匹配到的值可以被指定类型，如果没有指定默认为str。同时记住不要在开头添加'/'。
    /articles/2003/ 会匹配第一个入口，因为是按顺序来的
    /articles/2003/03/ 会匹配第三个，即调用views.xxx(request,year=2005,month=3)
    /articles/2003 不匹配任何入口，因为上述四个入口都要求'/'结尾
## 路径转换器
    主要有以下几种：
        str：匹配任何除了'/'的非空字符串
        int：匹配任何非0的正值，返回一个整型值
        slug：匹配任何由ASCII的'-','_',字母,数字组成的slug string???
        uuid：匹配一个格式化的uuid，阻止多个url匹配至一个相同页面。其应包含'-'且字母均为小写，返回uuid实例。
        path：匹配任何非空字符串，包括'/'。相比从url中截取一段作为str，这种方法可以匹配完整的url。
    为了适应更复杂的场景，还可以注册自己的路径转换器。转换器是一个类，并且包含：
        一个regex类属性，作为string
        一个to_python(self,value)方法，将匹配的字符转为传入视图函数的参数，如果不能转换，会引发ValueErorr异常，如果没有与之匹配的url，应拿出404
        一个to_url(self,value)方法，将python的数据类型转换为url可用的字符串。
    下面是个自定义转换器的例子：
        class FourDigtalYearConverter:
            regex = '[0-9]{4}'
            def to_python(self,value):
                return int(value)
            def to_url(self,value):
                return '%04d' % value
    然后需要注册这个自定义转换器：
        from django.urls import path,register_converter
        from . import FourDigtalYearConverter,views
        register_convert(FourDigtalYearConverter,'yyyy')
        urlpatterns=[...path('articles/<yyyy:year',views.xxx)...]
# 使用RE
    如果路径和转换器语法不足以定义你的url，便要用到正则表达式了，使用时需要用re_path()代替path(),像这样：
        path('articles/2003/',view.xx)
        re_path(r'articles/(?P<year>[0-9]{4})/$'.view.xxx)
        re_path(r'articles/(?P<slug>[\w-I+)/$')???
    以上对比之前的例子实际有些缺憾，比如年份被限制为了4位数，每个传入视图函数的参数类型都将转为str。所以在使用re_path和path()相互替换时要特别注意视图函数变量的类型是否被改变。
    当没有组命名时，你可使用更简单的RE，比如[0-9]{4},但不是很推荐