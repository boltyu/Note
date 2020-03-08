# Private key
    example:
    openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem
    req:PKCS#10 X.509 Certificate Signing Request (CSR) Management.

    [cert like this](example/certificate.pem)
    [key like this](example/key.pem)

# Code
    以下代码是最小TSL服务器的例子。第一件要做的事是在init_openssl()函数中通过加载错误信息需要用到的字符串来初始化openssl，还有哦诶之TLS所需的算法。
    然后我们创建一个SSL_CTX或者 SSL的context。此步骤使用SSLv23_server_method，尽管它的名字实际也限制了服务器所能使用SSL/TLS的最高版本。
    接着配置context，我们使用SSL_CTX_set_ecdh_auto告诉openssl为我们选择椭圆曲线（这个函数在之前的版本中不可用，只能手动来做）。最后为context指定证书和私钥。
    再接着我们用平常使用socket的方法来创建一个新的服务，此时与openssl还没有关系。当我们使用accept获取了一个新连接，我们创建一个SSL结构体来处理TLS，用它来存储这个新连接的信息。我们使用SSL_set_fd告诉openssl进行通讯时使用的文件描述符。在这个例子中，我们使用SSL_accept处理服务端的TLS握手，SSL_write发送我们的消息，最终，清理以上结构体。
    [server like this](example/TLSserver.c)
    [client like this](example/TLSclient.c)


# Reference
    https://www.ibm.com/support/knowledgecenter/SSMNED_5.0.0/com.ibm.apic.cmc.doc/task_apionprem_gernerate_self_signed_openSSL.html