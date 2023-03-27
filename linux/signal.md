# signal， note on APUE-3rd-10

    一般信号值不为0，kill函数会在特定应用下使用信号0
    SIGKILL SIGSTOP 无法被忽略，因为要确保kernel或superuser可以杀掉进程。
    忽略一些硬件异常（如非法内存访问和除0）会导致进程处于未知状态
    或许可以在 SIGTERM 信号到来时处理进程退出资源

## signal(int signo, void (*func)(int))

    func 可以是 SIG_IGN，SIG_DFL 或一个函数地址

## interrupted system calls

## reentrant functions

## kill and raise

## sigaction

## sa_flags

1. SA_INTERRUPT 被中断的系统调用不会再执行
2. ...
3. SA_ONSTACK 如果通过sigaltstack指定了替用stack，则信号再替用stack上传递给进程
