# bash_history backup
    sudo chmod derootfs
    sudo chroot derootfs/
    cd derootfs/
    cd ../
    sudo chroot derootfs/
    ls rootfs
    rm rootfs.tar
    rm derootfs/ -rf
    sudo rm derootfs/ -rf
    sudo debootstrap --arch=armhf --foreign buster derootfs
    sudo cp /usr/bin/qemu-arm-static /mnt/usr/bin/
    sudo cp /usr/bin/qemu-arm-static derootfs/
    sudo chroot derootfs/ /usr/bin/qemu-arm-static /bin/sh -i
    sudo mv derootfs/qemu-arm-static derootfs/usr/bin/
    sudo chroot derootfs/ /usr/bin/qemu-arm-static /bin/sh -i
    sudo chroot derootfs/ /usr/bin/qemu-arm-static
    sudo chroot derootfs/ /usr/bin/qemu-arm-static -i
    sudo chroot derootfs/ /usr/bin/qemu-arm-static root
    sudo chroot derootfs/ /usr/bin/qemu-arm-static /bin/sh root
    sudo chroot derootfs/ /usr/bin/qemu-arm-static
    sudo chroot derootfs/ /usr/bin/qemu-arm-static /bin/sh -i
    sudo chroot derootfs/ /usr/bin/qemu-arm-static /bin/sh root
    sudo chroot derootfs/ /usr/bin/qemu-arm-static /bin/sh -i
    ls
    exit
    sudo minicom -b 115200 -D /dev/ttyUSB1
    sudo minicom -b 115200 -D /dev/ttyUSB0
    exit
    sudo apt update
    sudo apt install qemu-user-static
    cd ~
    ls
    cd Works/
    ls
    cd ../
    ls
    mkdir derootfs
    cd derootfs/
    sudo apt install debootstrap
    sudo apt install qemu-user-static
    debootstrap --arch=armhf --foreign buster ./
    sudo debootstrap --arch=armhf --foreign buster ./
    cp /usr/bin/qemu-arm-static usr/bin/
    sudo cp /usr/bin/qemu-arm-static usr/bin/
    sudo chroot /mnt/
    sudo chroot .
    chroot . /usr/bin/qemu-arm-static /bin/sh -i
    sudo chroot . /usr/bin/qemu-arm-static /bin/sh -i
    cd ../
    ls
    rm derootfs/ -rf
    sudo rm derootfs/ -rf
    ls
    debootstrap --arch=armhf --foreign buster derootfs
    sudo debootstrap --arch=armhf --foreign buster derootfs
    cp /usr/bin/qemu-arm-static derootfs/usr/bin/
    sudo cp /usr/bin/qemu-arm-static derootfs/usr/bin/
    sudo chroot derootfs/
    sudo cp /usr/bin/qemu-arm-static derootfs/usr/bin/
    sudo chroot derootfs/ /usr/bin/qemu-arm-static /bin/sh -i
    ls
    cd rootfs/
    cd ../
    tar cvf rootfs.tar derootfs/
    rm rootfs.tar
    sudo tar cvf rootfs.tar derootfs/
    du -sh rootfs