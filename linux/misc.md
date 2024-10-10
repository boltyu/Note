# 问题

#### can't execute ... no such file or directory

一个思路是通过 file 命令查看程序依赖项目，然后继续查找问题。本次是因为在 64bit ubuntu 中执行 32bit 程序，出现上述错误，实则缺少 /lib/ld-linux.so.2，通过以下方式安装
sudo dpkg --add-architecture i386
sudo apt update
sudo apt-get install libc6:i386
