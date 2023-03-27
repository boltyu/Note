# 设置接收函数超时时间

    struct timeval tv = {1, 0};
    ret = setsockopt(s, SOL_SOCKET, SO_RCVTIMEO, (const char*)&tv, sizeof(tv));
