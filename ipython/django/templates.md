# 模版
作为一个web框架，django需要一个便捷的方式来动态生成HTML。最通用的方式是模版。模版包含了静态部分和一些特定语法来描述动态内容如何被插入。在Tutorial3中有手把手教程。
Django工程可以配置一个或多个模版引擎，也可以不用。Django定义了一个标准API在渲染模版时可以不考虑后端类型。渲染在这里的意思是把内容插入到模版中然后返回结果。
# 配置项
DIRS定义了一些路径，模版引擎会在其中寻找模版。
APP_DIRS告诉引擎是否要去APP路径中寻找。
NAME如果你有多个引擎需要配置，请以NAME来区分。
OPTIONS包含了后端特定的一些配置。

# django.template.loader模块
get_template(template_name,using=None)
这个通过指定名称来家在模版，并返回一个Template对象。具体返回值决定于后端，后端有自己的Template类。这个函数会顺序利用每个模版引擎查找模版，如果还是没找到就引发TemplateDoseNotExist。如果模版找到了但是有无效语法，则引发TemplateSyntaxError。模版如何查找和加载取决于后端和配置。
select_template(template_name_list,using=None)
与get_template一样，不同之处在于它以模版名称列表作为参数，顾名思义它会在列表中选择一个模版，这个方法非常灵活，见下面这个官方例子：
	select_template(['story_%s_detail.html' % story.id, 'story_detail.html'])
# django模版语言概览
## 变量
	{{ variables }}
字典数据可以使用点查找
	{{ my_dict.key }}
	{{ my_object.attribute }}
	{{ my_list.0 }}
## Tags
	{% Tags %}
Tags为渲染提供决定性逻辑。 
	{% csrf_token %}
Tags也可以接受参数
	{% cycle 'odd' 'even' %}
## 过滤器 |
	{{ django|title }}
上述过滤器会将django中单词都变为首字母大写。
	{{ my_date|date:"Y-m-d" }}
## 注释
	{# this won't be rendered #}
以上为单行注释
	{% comment %} {% endcomment %}
以上为多行注释

#模版继承
说明书称此项功能为django模版强大特色之一，base模版中我们可以先不实现具体功能，而是用block先占位。
在具体实现模版中，先
	{% extends 'base.html' %}
再定义block内的具体实现。

# csrf_token
此项用于CSRF保护

# cycle
每次遇到这个Tag时便产生一个它的变量，第一次遇到时产生第一个变量，当所有变量都遍历后，回到第一个重新产生，看下面这个例子
	{% for o in some_list %}
		<tr class="{% cycle 'row1' 'row2' %}">
		</tr>
	{% endfor %}
上例中第一次迭代使用了class row1，第二次是row2，第三次又回到row1，当然上述row1和row2不加引号则表示变量，当然cycle中的变量会被转译，我们只要使用auto-escaping标签来关闭转译即可
	{% for o in some_list %}
		<tr class="{% autoescape off %}{% cycle row1 row2 %}{% endautoescape %}">
		</tr>
	{% endfor %} 
命名和再引用
	{% cycle 'row1' 'row2' as rowcolors %}
	{{ rowcolors }}
	{% cycle rowcolors %}
先命名但暂时不引用
	{% cycle 'row1' 'row2' as rowcolors silent %}
重置cycle
	{% resetcycle rowcolors %}

# debug
输出包括context和modules的调试信息

# extends
此Tag指定其父模版，extends后可加父模版名称，也可加变量，变量亦可指定父模版名称，或是本身就是个Tmeplate对象。名称路径要使用相对路径，比如可以是
	{% extends "./base2.html" %}

# filter
	{% filter force_escape|lower %}
		This text will be HTML-escaped, and will appear in all lowercase.
	{% endfilter %}
要注意escape和safe这两个过滤器不接受参数，所以用autoescape标签代替好了。safe这样用
	{% firstof var1 var2|safe %}

# firstof
	{% firstof var1 var2 var3 %}
输出第一个不是false的变量，如果都是false就啥也不输出。
	{% firstof var1 var2 var3 "fallback value" %}
上例改进了一下，都是false时会提示‘fallback value’
注意此Tag也会自动转译变量值。

# for
	{% for athlete in athlete_list %}
		<li>{{ athlete.name }}</li>
	{% endfor %}
还可以反着遍历
	{% for athlete in athlete_list reversed %}
嵌套列表和字典可进一步解包
	{% for key, value in data.items %}
	{{ key }}: {{ value }}
forloop.counter forloop.counter0 forloop.first forloop.last 这些是循环里可用的一些预设变量
# for...empty
	{% for ...%}
	{% empty %}
当循环目标为空或不存在，执行empty下面内容
# if
可与and not or联合使用来做逻辑判断，and优先级高于or，甚至==,!=,<,>,>=,<=,in,not in,is,is not都可以用 

# ifchanged
测试迭代的变量是否发生了变化，这个Tag只能用在循环里，与if一样，也可以带个else小跟班

# include
	{% include "foo/bar.html" %}
加载一个模版并用当前context渲染它，模版名称可以是字符串也可以是变量，路径可以像上例相对于模版加载器的根路径，也可以使用./ ../。
	{% include "t.html" with name='ttt' %}
如上你也可以指定context内容
	{% .... only %}
如果使用only则表示不使用当前context的内容，但如果有with，仍然使用with给出的内容

# load
加载一个自定义的模版标签集。
	{% load somelibrary package.otherlibrary %}
上例会加载somelibrary和package包里otherlibrary中所有tag和过滤器
	{% load ... from ... %}
加载特定内容

# lorem
显示随机的 lorem ipsum 拉丁文本，这在提供样本数据时会有用的。

# now
显示当前日期或时间，日期格式化见date过滤器描述

# regroup
重分组以分类数据

# resetcycle
重置cycle从第一个项目开始

# spaceless
移除空格

# templatetag
输出一项模版标签，比如openblock即{%

# url
返回绝对路径，例如
	path('client/<int:id>/', app_views.client, name='app-views-client')
	{% url 'app-views-client' client.id %}
	/clients/client/123/
一样可以使用as将其暂存以便后续使用
还有如新手教程所说的，在:左侧指定命名空间

# verbatim
阻止模版引擎渲染其中内容

# widthratio

# with

# django内置的一些过滤器
##

# static
	{% load static %}
	{% get_static_prefix as STATIC_PREFIX %}

	<img src="{{ STATIC_PREFIX }}images/hi.jpg" alt="Hi!">
	<img src="{{ STATIC_PREFIX }}images/hi2.jpg" alt="Hello!">

#
