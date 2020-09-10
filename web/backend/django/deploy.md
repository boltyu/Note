# 使用check
    manage.py check --deploy
    以上命令可以帮助检查
# 关于secret_key
    密码必须是一个较长的随机字符串，需要妥善保存，比如不要提交至版本控制中，或者硬编码在程序中，或者保存在一个文件里
# debug模式
    不在开发模式应关闭debug
# 关于一些特定的环境变量
## ALLOWED_HOSTS
    当debug关闭时，没有正确配置allowed_hosts值时django不会工作。
    这项配置为了保护你免受一些CSRF攻击，如果你使用了通配符，你可能需要自己去验证HOST http的头部，否则要保证你的站点在此类攻击下的强韧性。
    你所使用的web服务器一样需要配置验证主机功能，忽略错误主机请求、返回静态错误页等等，确保web服务器不会进一步将这些错误请求传给django。比如在nginx上，有个默认主机，为它配置444 no response：
        server{
            listen 80 default_server;
            return 444;
        }
## CACHES
    如果使用了缓存，链接参数在开发和应用模式可能会不一样？
    缓存服务器通常是弱校验，此时要确保它只接收从你的应用服务器发起的连接。
## DATABASES
    数据库连接参数也能是两种模式下有些不同。
    数据库密码非常敏感，应该像保护secret_key一样保护它。
    为了安全，要确保数据库服务器仅接收你的应用服务器发起的连接。
    还有如果没有配置备份的话，赶紧去配置呀
## EMAIL_BACKEND
    如果你的站点有发送邮件，以下都要设置正确。
    默认django会从webmaster@localhost和root@localhost发送邮件，然而一些邮件服务商拒绝这些地址，为了使用其它发送地址，要修改DEFAULT_FROM_EMAIL和SERVER_EMAIL设置
## STATIC_ROOT 和 STATIC_URL
    开发模式中静态文件会自动管理，而在产品应用中，必须指定STATIC_ROOT路径，然后collectstatic会帮你拷贝
    详见[https://docs.djangoproject.com/en/3.0/howto/static-files/]
## MEDIA_ROOT 和 MEDIA_URL
    媒体文件是由用户上传的，要警惕对待这些文件，确保你的web服务器不会去运行或者解释他们，比如用户上传.php，要让web服务器不去执行它。

# HTTPS
    任何允许用户登录的站点应强制使用HTTPS以避免tokens等泄漏。
    django中token包含用户名密码，session cookie，还有密码重置token。（假如你要使用邮件发送这些信息的话，那保护工作可能就有限了)
    保护敏感区域内容仍然不够，应为同一cookie可能会在HTTP和HTTPS中都使用。你的网络服务器需要拒绝掉HTTP，只把HTTPS给django
    一旦你设置完HTTPS，要把以下设置也打开：
## CSRF_COOKIES_SECURE
    打开此项避免意外通过HTTP传输CSRF cookie
## SEESION_COOKIE_SECURE
    打开此项避免意外通过HTTP传输session cookie

# 体验优化
## Sessions
    考虑使用cached sessions来提升体验
    如果使用数据库存seesions的话，要记得清理旧session避免垃圾过多。
## CONN_MAX_AGE
    开启长久数据库连接可以加快后续的访问速度，这在有限带宽的虚拟主机上十分有效
## TEMPLATES
    开启模版缓存加载器通常会大幅提升性能，因为不用每次都渲染。详见模版加载器

# 错误报告
    django可以捕获错误并通知你
## LOGGING
    在发布产品前检阅你的logging配置，在运行一些时候之后尽快查询记录
## ADMINS 和 MANAGERS
    ADMINS 会从邮件通知你500错误
    MANAGERS 会通知你404错误，如果设置了IGNORABLE_404_URLS可以帮助你过滤一些错误
    考虑使用类似于Sentry的错误监视系统，它可以对错误log做一些聚合，避免你的收件箱被填乱

## 自定义默认的错误视图
    Django默认包含了多个HTTP错误代码的视图和模版。在你的模版根目录下新建404.html 500.html 403.html 和 400.html来覆盖系统的默认视图。
