# Running A Full Node - Linux Instructions
    https://bitcoin.org/en/full-node#linux-instructions
# Run a Bitcoin Core full node on CentOS 7
    https://ma.ttias.be/run-a-bitcoin-core-full-node-on-centos-7/
# centos7安装BitCoin客户端
    https://www.cnblogs.com/sky-cheng/p/11976727.html
# 官网
    https://bitcoincore.org/zh_CN/
# bitcoin.conf 一些解释
    https://github.com/ElementsProject/elements/blob/master/share/examples/bitcoin.conf

# snap方法安装bitcoin-core
    Install bitcoin-core on CentOS -- snap
    https://snapcraft.io/install/bitcoin-core/centos

# 比特币核心部署 - bitcoin core for linux
    https://cloud.tencent.com/developer/article/1806254

    sudo -i
    wget https://bitcoin.org/bin/bitcoin-core-0.13.0/bitcoin-0.13.0-x86_64-linux-gnu.tar.gz
    wget https://bitcoin.org/bin/bitcoin-core-25.0/bitcoin-25.0-x86_64-linux-gnu.tar.gz
    tar -zvxf bitcoin-25.0-x86_64-linux-gnu.tar.gz

    install -m 0755 -o root -g root -t /usr/local/bin bitcoin-25.0/bin/*

    mkdir ~/.bitcoin
    touch ~/.bitcoin/bitcoin.conf
    chmod 600 ~/.bitcoin/bitcoin.conf

    echo rpcuser=a >> ~/.bitcoin/bitcoin.conf
    echo rpcpassword=b >> ~/.bitcoin/bitcoin.conf


    yum -y install epel-release
    bitcoind: /lib64/libm.so.6: version `GLIBC_2.27' not found (required by bitcoind)
    [root@aws-jp-zf-test-bib-lhqer01 ~]# ldd --version
    ldd (GNU libc) 2.17
    Copyright (C) 2012 Free Software Foundation, Inc.
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    Written by Roland McGrath and Ulrich Drepper.
    [root@aws-jp-zf-test-bib-lhqer01 ~]# gcc --version
    gcc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44)
    Copyright (C) 2015 Free Software Foundation, Inc.
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# 直接安装 GCC-8
    $ yum install -y devtoolset-8-gcc devtoolset-8-gcc-c++ devtoolset-8-binutils
    这个没反应

# 接下来试试这个
    http://www.pdsmlme.com.cn/?p=112
    这个好使： https://www.cnblogs.com/dingshaohua/p/17103654.html

    wget http://ftp.gnu.org/gnu/glibc/glibc-2.28.tar.gz
    tar xf glibc-2.28.tar.gz 

    configure: error: 
    *** These critical programs are missing or too old: make bison compiler
    *** Check the INSTALL file for required versions.


    /usr/bin/ld: cannot find -lnss_test2

# /usr/bin/ld: cannot find -lnss_test2
    centos7 升级 glibc && gcc
    貌似好使：https://garlicspace.com/2020/07/18/centos7-%E5%8D%87%E7%BA%A7-glibc-gcc/

# 删除build文件夹重新来

# 新的错误 /lib/../lib64/libnss_nis.so: undefined reference to `_nsl_default_nss@GLIBC_PRIVATE'
    test ! -x /root/glibc-2.28/build/elf/ldconfig || LC_ALL=C \
    /root/glibc-2.28/build/elf/ldconfig  \
                            /lib64 /usr/lib64
    LD_SO=ld-linux-x86-64.so.2 CC="gcc -B/usr/bin/" /usr/bin/perl scripts/test-installation.pl /root/glibc-2.28/build/
    /lib/../lib64/libnss_nis.so: undefined reference to `_nsl_default_nss@GLIBC_PRIVATE'
    collect2: error: ld returned 1 exit status
    Execution of gcc -B/usr/bin/ failed!
    The script has found some problems with your installation!
    Please read the FAQ and the README file and check the following:
    - Did you change the gcc specs file (necessary after upgrading from
    Linux libc5)?
    - Are there any symbolic links of the form libXXX.so to old libraries?
    Links like libm.so -> libm.so.5 (where libm.so.5 is an old library) are wrong,
    libm.so should point to the newly installed glibc file - and there should be
    only one such link (check e.g. /lib and /usr/lib)
    You should restart this script from your build directory after you've
    fixed all problems!
    Btw. the script doesn't work if you're installing GNU libc not as your
    primary library!
    make[1]: *** [Makefile:111: install] Error 1
    make[1]: Leaving directory '/root/glibc-2.28'
    make: *** [Makefile:12: install] Error 2
    [root@aws-jp-zf-test-bib-lhqer01 build]#


    mkdir build  && cd build
    ../configure --prefix=/usr --disable-profile --enable-add-ons --with-headers=/usr/include --with-binutils=/usr/bin --enable-obsolete-nsl

# bitcoin-cli --version
    Bitcoin Core RPC client version v25.0.0
    Copyright (C) 2009-2023 The Bitcoin Core developers

    Please contribute if you find Bitcoin Core useful. Visit
    <https://bitcoincore.org/> for further information about the software.
    The source code is available from <https://github.com/bitcoin/bitcoin>.

    This is experimental software.
    Distributed under the MIT software license, see the accompanying file COPYING
    or <https://opensource.org/licenses/MIT>

# bitcoind --version
    Bitcoin Core version v25.0.0
    Copyright (C) 2009-2023 The Bitcoin Core developers

    Please contribute if you find Bitcoin Core useful. Visit
    <https://bitcoincore.org/> for further information about the software.
    The source code is available from <https://github.com/bitcoin/bitcoin>.

    This is experimental software.
    Distributed under the MIT software license, see the accompanying file COPYING
    or <https://opensource.org/licenses/MIT>

# ls /usr/local/bin/
    bitcoin-cli  bitcoin-qt  bitcoin-tx  bitcoin-util  bitcoin-wallet  bitcoind  test_bitcoin

    在/usr/local/bin/下会生成以下几个文件
    bitcoin-cli ：是Bitcoind的一个功能完备的RPC客户端，包括查询区块，交易信息等等
    bitcoind ：是比特币运行的核心程序俗称bitcoin core
    bitcoin-tx ：比特币交易处理模块，支持交易的查询和创建
    bench_bitcoin ：根据https://github.com/bitcoin/bitcoin/issues/829 解释，作用是编译系统更新，也就是检查系统使用的一些加密算法是否有新的更新
    test_bitcoin ：运行各个模块的测试代码

# 默认配置文件
    tail ~/bitcoin-25.0/bitcoin.conf
    [main]

    # Options for testnet
    [test]

    # Options for signet
    [signet]

    # Options for regtest
    [regtest]

# 配置
    sudo -i
    mkdir /data/bitcoin
    touch /data/bitcoin/bitcoin.conf
    chmod 600 /data/bitcoin/bitcoin.conf

    echo rpcuser=a >> /data/bitcoin/bitcoin.conf
    echo rpcpassword=b >> /data/bitcoin/bitcoin.conf
    echo txindex=1 >> /data/bitcoin/bitcoin.conf
    echo server=1 >> /data/bitcoin/bitcoin.conf
    echo listen=1 >> /data/bitcoin/bitcoin.conf
    echo irc=1 >> /data/bitcoin/bitcoin.conf
    echo upnp=1 >> /data/bitcoin/bitcoin.conf
    echo port=8332 >> /data/bitcoin/bitcoin.conf
    echo rpcport=8333 >> /data/bitcoin/bitcoin.conf
    echo dbcache=40960 >> /data/bitcoin/bitcoin.conf
    echo rpcallowip=127.0.0.1 >> /data/bitcoin/bitcoin.conf
    echo datadir=/data/bitcoin/data >> /data/bitcoin/bitcoin.conf

    tail /data/bitcoin/bitcoin.conf

# 配置解释
    接受JSON-RPC请求
    server=1
    是否是独立进程，守护进程
    daemon=1
    测试网络
    testnet=1
    最大连接数    maxconnections=1
    rpc 用户名
    rcpuser=testuser
    密码
    rpcpassword=123456
    允许访问
    rpcallowip=127.0.0.1
    端口
    rpcport=8332
    数据存储位置
    datadir=/home/bitcoin/data

# 后台运行
    bitcoind -daemon
    bitcoind -conf=/data/bitcoin/bitcoin.conf 
    bitcoind -conf=/data/bitcoin/bitcoin.conf -daemon
# 查看数据目录
ls /data/bitcoin/

# 查看磁盘
    df -hl
    Filesystem      Size  Used Avail Use% Mounted on
    devtmpfs         32G     0   32G   0% /dev
    tmpfs            32G     0   32G   0% /dev/shm
    tmpfs            32G   57M   32G   1% /run
    tmpfs            32G     0   32G   0% /sys/fs/cgroup
    /dev/xvda1       30G  6.9G   24G  23% /
    /dev/xvdb1      2.0T   33M  2.0T   1% /data
    tmpfs           6.3G     0  6.3G   0% /run/user/1001


    ls /root/.bitcoin
    ls /data/bitcoin/data
# 查看日志
    tail -f /data/bitcoin/data/debug.log
    日志文件位于/home/bitcoin/data/testnet3/目录下的debug.log中，查看日志
# bitcoin-cli 

    bitcoin-cli -conf=/data/bitcoin/bitcoin.conf stop
    bitcoin-cli -conf=/data/bitcoin/bitcoin.conf getnetworkinfo              #查看网络状态
    bitcoin-cli-conf=/data/bitcoin/bitcoin.conf getpeerinfo                 #查看网络节点
    bitcoin-cli-conf=/data/bitcoin/bitcoin.conf getblockchaininfo           #查看区块链信息：如同步进度
    bitcoin-cli-conf=/data/bitcoin/bitcoin.conf help                        #查看所有命令

# 查看某个文件夹的瓷盘占用
    rm -rf /root/.bitcoin
    du -sh /root/.bitcoin
    du -sh /data/bitcoin/data
# 查看进程
    ps aux | grep bitcoind
    root      85432  100  0.5 2019112 352756 ?      Rsl  13:47   0:05 bitcoind -conf=/data/bitcoin/bitcoin.conf -daemon
    root      85460  0.0  0.0 112740   948 pts/0    S+   13:47   0:00 grep --color=auto bitcoind