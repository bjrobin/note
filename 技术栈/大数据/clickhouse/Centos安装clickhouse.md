# 官方安装文档
    Install ClickHouse
    https://clickhouse.com/docs/en/install


# sse4_2
    验证当前服务器的 CPU 是否支持 SSE 4.2 指令集，因为向量化执行需要用到这项特性：
    grep -q sse4_2 /proc/cpuinfo && echo "支持 SSE 4.2 指令集" || echo "不支持 SSE 4.2 指令集"
# 安装
    sudo yum install -y yum-utils
    sudo yum-config-manager --add-repo https://packages.clickhouse.com/rpm/clickhouse.repo
    sudo yum install -y clickhouse-server clickhouse-client

    sudo /etc/init.d/clickhouse-server start
    clickhouse-client # or "clickhouse-client --password" if you set up a password.
# 这些可以不用
    systemctl enable clickhouse-keeper
        Created symlink from /etc/systemd/system/multi-user.target.wants/clickhouse-keeper.service to /usr/lib/systemd/system/clickhouse-keeper.service.
    systemctl start clickhouse-server
    systemctl status clickhouse-server
    clickhouse-client # or "clickhouse-client --password" if you set up a password.

# <Error> Application: Code: 430. 
    2024.04.22 18:27:08.951056 [ 21851 ] {} <Error> Application: Code: 430. DB::Exception: Effective user of the process (root) does not match the owner of the data (clickhouse). Run under 'sudo -u clickhouse'. (MISMATCHING_USERS_FOR_PROCESS_AND_DATA), Stack trace (when copying this message, always include the lines below):

# 其他命令
    启动服务、停止服务（任意目录下均可）
    service clickhouse-server start
    service clickhouse-server stop
    启动
    sudo /etc/init.d/clickhouse-server start
    停止
    sudo /etc/init.d/clickhouse-server stop
    重启
    sudo /etc/init.d/clickhouse-server restart
    启动之后查看服务状态
    service clickhouse-server status
    连接clickhouse
    clickhouse-server
    clickhouse-client -m --password <密码>
    退出客户端连接
    ctrl+z


# 把数据存放目录都配置到 /data/clickhouse/ 目录下面。
    vim /etc/clickhouse-server/config.xml
# Configuration Files
    https://clickhouse.com/docs/en/operations/configuration-files

    <log>/data/log/clickhouse-server/clickhouse-server.log</log>
    <errorlog>/data/log/clickhouse-server/clickhouse-server.err.log</errorlog>
    <custom_cached_disks_base_directory>/data/clickhouse/caches/</custom_cached_disks_base_directory>
    <path>/data/clickhouse/</path>
    <tmp_path>/data/clickhouse/tmp/</tmp_path>
    <user_files_path>/data/clickhouse/user_files/</user_files_path>
    <format_schema_path>/data/clickhouse/format_schemas/</format_schema_path>

# 日志文件

    tail -f /var/log/clickhouse-server/clickhouse-server.log
    tail -f /var/log/clickhouse-server/clickhouse-server.err.log
    ls -l /var/log/
        drwxr-xr-x  2 clickhouse clickhouse      68 Apr 23 14:27 clickhouse-keeper
        drwxr-xr-x  2 clickhouse clickhouse     104 Apr 23 13:19 clickhouse-server


# 参考：ClickHouse安装以及使用
    https://juejin.cn/post/7065087471247163405
# 默认原始文件 
    https://github.com/ClickHouse/ClickHouse/blob/master/programs/server/config.xml

# 修改完之后重启服务：
    service clickhouse-server restart
    systemctl start clickhouse-server


# yum 命令无反应的解决方法
## 已安装
    yum list installed | grep clickhouse
## 清理yum缓存
    yum clean all
## 或删除cache目录
    rm -rf /var/cache/yum/*

## 卸载及删除安装文件（需root权限）
    
    yum remove -y clickhouse-common-static
    yum remove -y clickhouse-server-common
    rm -rf /var/lib/clickhouse
    rm -rf /etc/clickhouse-*
    rm -rf /var/log/clickhouse-server
    rm -rf /var/log/clickhouse-keeper

# 修改配置
    <path>/var/lib/clickhouse/</path>
    # 1.打开listen_host，二选一
    # 如果支持IPV6
    <listen_host>::</listen_host>
    # 如果支持IPV4
    <listen_host>0.0.0.0</listen_host>
    # 2.修改端口号，9000被python占用
    <tcp_port>9099</tcp_port>

    默认数据文件路径：<path>/var/lib/clickhouse/</path>
    默认日志文件路径：<log>/var/log/clickhouse-server/clickhouse-server.log</log>

# 启动失败

    systemctl start clickhouse-server
    Job for clickhouse-server.service failed because the control process exited with error code. See "systemctl status clickhouse-server.service" and "journalctl -xe" for details.

    systemctl status clickhouse-server.service
    ● clickhouse-server.service - ClickHouse Server (analytic DBMS for big data)
    Loaded: loaded (/usr/lib/systemd/system/clickhouse-server.service; enabled; vendor preset: disabled)
    Active: activating (auto-restart) (Result: exit-code) since Mon 2024-04-22 18:07:03 HKT; 29s ago
    Process: 16988 ExecStart=/usr/bin/clickhouse-server --config=/etc/clickhouse-server/config.xml --pid-file=%t/%p/%p.pid (code=exited, status=127)
    Main PID: 16988 (code=exited, status=127)

    Apr 22 18:07:03 aws-jp-zf-test-bib-lhqer01 systemd[1]: Failed to start ClickHouse Server (analytic DBMS for big data).
    Apr 22 18:07:03 aws-jp-zf-test-bib-lhqer01 systemd[1]: Unit clickhouse-server.service entered failed state.
    Apr 22 18:07:03 aws-jp-zf-test-bib-lhqer01 systemd[1]: clickhouse-server.service failed.

clickhouse数据目录路径问题
https://blog.csdn.net/qq_41286972/article/details/113767443


# 修改权限
chown -R clickhouse:clickhouse /var/log/clickhouse-keeper
chown -R clickhouse:clickhouse /var/log/clickhouse-server
chown -R root:root /var/lib/clickhouse
chown -R clickhouse:clickhouse /var/lib/clickhouse
ls -l /var/lib
# failed
    不可以：
    systemctl start clickhouse-server
    Job for clickhouse-server.service failed because the control process exited with error code. See "systemctl status clickhouse-server.service" and "journalctl -xe" for details.

    可以：
    /usr/bin/clickhouse-server --config-file=/etc/clickhouse-server/config.xml
    clickhouse-server --config-file=/etc/clickhouse-server/config.xml
# systemctl enable clickhouse-keeper
Created symlink from /etc/systemd/system/multi-user.target.wants/clickhouse-keeper.service to /usr/lib/systemd/system/clickhouse-keeper.service.

netstat -tunlpa | grep 9000

# 正确
    sudo clickhouse start
    sudo service clickhouse-server start
    sudo clickhouse stop



# 参考：
    clickhouse数据目录路径问题
    https://blog.csdn.net/qq_41286972/article/details/113767443

    ####复制数据目录到新的路径
    cp /var/lib/clickhouse -r /data
    cp /var/log/clickhouse-server -r /data/clickhouse-log
    cp /var/log/clickhouse-keeper -r /data/clickhouse-log


    ####删除原来文件夹的文件
    rm -rf /var/lib/clickhouse/*
    rm -rf /var/log/clickhouse-server
    rm -rf /var/log/clickhouse-keeper
    ####建立软连接
    ln -s  /data/clickhouse/*  /var/lib/clickhouse
    ls /data/clickhouse-log /var/log/clickhouse-server
    ls /data/clickhouse-log /var/log/clickhouse-keeper
    ####给新的路径添加权限
    chown -R clickhouse.clickhouse /data/clickhouse
    chown -R clickhouse.clickhouse /data/clickhouse-log
    ####重启clickhouse
    sudo /etc/init.d/clickhouse-server restart
    sudo /etc/init.d/clickhouse-server start


# 安装python


    wget https://www.python.org/ftp/python/3.12.3/Python-3.12.3.tgz
    tar -zxvf Python-3.12.3.tgz
    cd Python-3.12.3/

    ./configure --prefix=/usr/local/python3.9 --with-ssl


    ln -s /soft/Python-3.12.3/python3/bin/python3 /usr/bin/python3
    ln -s /soft/Python-3.12.3/python3/bin/pip3 /usr/bin/pip3

    ------------------------------------------
    https://blog.csdn.net/Skywin88/article/details/130519825
    #/bin/bash
    安装版本
    version=3.11.0

    yum install -y wget
    #只是将python3.11的安装包下载到 /root目录下
    wget https://www.python.org/ftp/python/${version}/Python-${version}.tgz
    #下载最新的软件安装包
    tar -xzf Python-${version}.tgz
    #安装EPEL（即企业版linux扩展包）
    yum -y install epel-release
    #解压缩安装包
    yum -y install gcc zlib zlib-devel libffi libffi-devel
    #安装源码编译需要的编译环境
    yum -y install readline-devel
    #可以解决后期出现的方向键、删除键乱码问题，这里提前避免。
    yum -y install openssl-devel openssl11 openssl11-devel
    #安装openssl11，后期的pip3安装网络相关模块需要用到ssl模块。
    export CFLAGS=$(pkg-config --cflags openssl11)
    export LDFLAGS=$(pkg-config --libs openssl11)
    #设置编译FLAG，以便使用最新的openssl库
    cd Python-${version}
    #进入刚解压缩的目录
    ./configure --prefix=/usr/local/python-3.12.3 --with-ssl
    #指定python3的安装目录为 /usr/python 并使用ssl模块，指定目录好处是
    #后期删除此文件夹就可以完全删除软件了。
    make
    make install
    #就是源码编译并安装了，时间会持续几分钟。
    mv /usr/bin/python3 /usr/bin/python3_bak
    mv /usr/bin/pip3 /usr/bin/pip3_bak
    #指定链接，此后我们系统的任何地方输入python3就是我们安装的
    ln -s /usr/local/python-${version}/bin/python3 /usr/bin/python3
    ln -s /usr/local/python-${version}/bin/pip3 /usr/bin/pip3
    ————————————————
    卸载就只用删除/usr/local/python-${version}/文件夹就可以了。后面从新安装，在按照上面的步骤从新编译。


    sudo yum install wget make cmake gcc bzip2-devel libffi-devel zlib-devel
    可以使用以下命令从包组安装所有开发工具

    sudo yum -y groupinstall "Development Tools"
# 参考
    CentOS系统安装python3.12.0
    https://keeplearnlearn.com/2023/11/16/centos%E7%B3%BB%E7%BB%9F%E5%AE%89%E8%A3%85python3-12-0/

    https://gist.github.com/tao12345666333/9fed328429f05ab788625e8fbd9a47a4
    sudo yum install gdbm-devel tk-devel xz-devel sqlite-devel readline-devel bzip2-devel ncurses-devel zlib=devel


    sudo yum install tkinter
    sudo yum install python3-tkinter
    make clean
    Tkinter是Python中的标准GUI库，它提供了一个用于创建图形用户界面的工具包，可以用于创建窗口、按钮、文本框、菜单等各种控件，使用户可以通过鼠标或键盘与应用程序进行交互。 


    ln -s /usr/local/python3.12.3/bin/python3.12 /usr/bin/python3.12
    ln -s /usr/local/python3.12.3/bin/pip3.12 /usr/bin/pip3.12

# 按照包
    pip3.12 install psutil
    pip3.12 install clickhouse-driver
    pip3.12 install pandas
    pip3.12 install bitcoinrpc

# 大于100000个分区
    <merge_tree>
        <max_parts_in_total>1000000</max_parts_in_total>
    </merge_tree>
# 后台运行入库程序
    sudo -i
    cd /data/script
    python3.12 01.py
    nohup python3.12 01.py
    nohup python3.12 -u 01.py > test.log 2>&1 &
    nohup -u python3.12 01.py > test.log 2>&1 &
    nohup python3.12 -u 02.py > 02.log 2>&1 &
    rm -ef test.log
    tail -f 02.log
 

    *含义解释：
    nohup  不挂起的意思
    python  test.py   python运行test.py文件

    -u     代表程序不启用缓存，也就是把输出直接放到log中，没这个参数的话，log文件的生成会有延迟

    > test.log  将输出日志保存到这个log中

    2>1        2与>结合代表错误重定向，而1则代表错误重定向到一个文件1，而不代表标准输出； 
    2>&1      换成2>&1，&与1结合就代表标准输出了，就变成错误重定向到标准输出.

    &         最后一个& ，代表该命令在后台执行

    *命令运行后会有提示，示例：
    [1]   2880

    代表进程2880中运行。

    *查看nohub命令下运行的所有后台进程：
    jobs
    *查看后台运行的所有进程：
    ps -aux

    *查看后台运行的所有python 进程：
    ps aux |grep python
    或者

    ps -ef | grep python

    *删除进程
    kill -9  [进程id]

    -9  的意思是强制删除


# 查看入库进度
    sudo -i
    clickhouse-client
    select max(height) from btc.address_all
# 迭代
sudo -i
nohup python3.12 -u 02.py > 02.log 2>&1 &
tail -f 02.log