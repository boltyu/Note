# HTTP方法装饰器
    @require_http_methods(['GET','PSOT'])
如果条件不符，将返回django.http.HttpResponseNotAllowed
    @require_GET
    @require_POST
    @require_safe()
其中safe包含了GET和HEAD方法

# GZip 压缩
    @gzip_page
如果浏览器允许ggzip压缩，