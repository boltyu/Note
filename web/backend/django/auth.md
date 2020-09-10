# User对象
User对象是认证系统的核心，在Django的认证框架下仅能存在一个user类。比如superusers和admin的‘staff’用户都是用户对象，只是具有特殊属性而已，而非不同类的用户对象。user的主要属性有username password email first_name last_name

# 使用authenticate验证用户
    from django.contrib.auth import authenticate
    user = authenticate(request = None, username='',password='')
    user is None?
request是一个HttpRequest类的可选项。
这是个底层的验证方法，比如RemoteUserMiddelware就会用到此方法。
如果你在寻找一个用户登录的路子，不妨试试LoginView

# Permissions和Authorization
Django有内置的权限系统，它提供了将权限和用户及分组用户关联的方法
Permission不仅能为每个类型的对象设置，也能为特定的对象实例设置。
User对象的有两个many-to-many域，groups和user_permissions，他们决定用户可以访问的内容
    myuser.groups.set([group_list])
    myuser.groups.add(group, group, ...) myuser.groups.remove(group, group, ...) myuser.groups.clear() myuser.user_permissions.set([permission_list]) myuser.user_permissions.add(permission, permission, ...) myuser.user_permissions.remove(permission, permission, ...) myuser.user_permissions.clear()

# 模型中的 Meta 类
    


# login_required 装饰器
login_required(redirect_field_name='next', login_url=None)
    from django.contrib.auth.decorators import login_required
    @login_required
    def my_view(request):
        ...
如果用户没登录，重定向至settings.LOGIN_URL，在查询字符串中传入当前绝对路径，比如/accounts/login/?next=/polls/3/
如果用户已登录，