# 什么是FLASK
    flask是一个轻量级[WSGI(web server gateway interface)](https://wsgi.readthedocs.io/en/latest/what.html)，起初是为了包装Werkzeug和Jinja组件，后来成为了最受欢迎的python web应用框架之一。
# 最小程序
        from flask import Flask
        app = Flask(__name__)

        @app.route('/')
        def hello_world():
            return 'Hello World!'

        @app.route('/test/')
        def test_hello():
            return 'test hellooooooooo!'

        if __name__ == '__main__':
            app.run()

    导入FLask后，FLask()将会实例化WSGI应用，上例中参数__name__是应用模块的名称。
    @app.route()用来指定哪个目录将会触发接下来的函数
        if __name__ == '__main__'
    以上代码确保服务器只会在该脚本被 Python 解释器直接执行的时候才会运行，而不是作为模块导入的时候
        app.run(host='0.0.0.0')
    以上代码使服务器对外部网络可见
        app.debug = True
        app.run()  
        or
        app.run(debug=True)
    以上代码使程序可以调试
## URL变量
        @app.route('/user/<username>')
        def show_user_info(username):
            return 'User %s' % username
        @app.route('/post/<int:postid>')
        def show_post_id(postid):
            return 'Post %d' % postid
## HTTP方法
        @app.route('/login',methods=['GET','POST'])
        def login():
            if(request.method == 'POST'):
                username = request.form.get('yname') # query POST arg
            else:
                username = reuqest.args.get('yname') # query GET arg

# Session会话
    如果你有设置Flask.secret_key，你就可以在应用中使用sessions。
    用户可以看到session的内容，但不能修改它，除非他们知道secret_key，所以请确保key的复杂度和安全性。
    使用class flask.session访问当前的session：
        new 属性查看是否为新发生的
        modified 属性查看是否被修改
        permanent 属性被设置为True时，默认过期执行permanent_session_lifetime中保存的秒数，即31天。否则关闭浏览器即失效。
## 会话接口
    会话接口session interface提供了一个简单的方式来代替flask正使用的session植入方法。
    class flask.sessions.SessionInterface
        使用open_session() and save_session()来替换使用原有方法。
        open方法如果返回None，Flask将调用make_null_session()来创建一个session
        使用以下方式自己管理session
            flask.Flask.session_interface
            app= Flask(__name__)
            app.session_interface = MySessionInterface()
        http://www.pythondoc.com/flask/api.html#id7
        