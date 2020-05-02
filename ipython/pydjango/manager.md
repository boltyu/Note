# django-admin和manager.py
    manager随工程自动创建，做和django-admin相同的工作，也可通过指定DJANGO_SETTINGS_MODULE环境变量来指向你工程中的settings.py文件
    django-admin默认会随安装而配置到系统环境中，如果没有可以在site-packages/django/bin等安装位置中找到
    windows用户没有符号链接，可以复制修改系统环境变量或者复制文件到指定位置
    工作在一个单独的django项目时，manager更容易使用，如果在多个项目间走动，使用django-admin加DJANGO_SETTINGS_MODULE或者命令行--settings选项
