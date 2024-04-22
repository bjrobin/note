# 官方安装文档
    Install ClickHouse
    https://clickhouse.com/docs/en/install

# 安装
    Setup the RPM repository
    sudo yum install -y yum-utils
    sudo yum-config-manager --add-repo https://packages.clickhouse.com/rpm/clickhouse.repo
    yum install -y clickhouse-server clickhouse-client

    systemctl enable clickhouse-keeper
        Created symlink from /etc/systemd/system/multi-user.target.wants/clickhouse-keeper.service to /usr/lib/systemd/system/clickhouse-keeper.service.
    systemctl start clickhouse-server
    systemctl status clickhouse-server
    clickhouse-client # or "clickhouse-client --password" if you set up a password.

# 启动
    clickhouse-server --config-file=/etc/clickhouse-server/config.xml
    Processing configuration file '/etc/clickhouse-server/config.xml'.
    Logging trace to /var/log/clickhouse-server/clickhouse-server.log
    Logging errors to /var/log/clickhouse-server/clickhouse-server.err.log
    2024.04.22 18:27:08.592946 [ 21851 ] {} <Information> SentryWriter: Sending crash reports is disabled
    2024.04.22 18:27:08.593030 [ 21851 ] {} <Trace> Pipe: Pipe capacity is 1.00 MiB
    2024.04.22 18:27:08.675498 [ 21851 ] {} <Information> Application: Starting ClickHouse 24.3.2.23 (revision: 54484, git hash: 8b7d910960cc2c6a0db07991fe2576a67fe98146, build id: DA47C8C3B6BA55C4A326D4DD33ACED2DFEA5DA96), PID 21851
    2024.04.22 18:27:08.675707 [ 21851 ] {} <Information> Application: starting up
    2024.04.22 18:27:08.675739 [ 21851 ] {} <Information> Application: OS name: Linux, version: 5.4.208-1.el7.elrepo.x86_64, architecture: x86_64
    2024.04.22 18:27:08.680730 [ 21851 ] {} <Information> Application: Available RAM: 62.79 GiB; physical cores: 16; logical cores: 16.
    2024.04.22 18:27:08.680786 [ 21851 ] {} <Information> Application: Available CPU instruction sets: SSE, SSE2, SSE3, SSSE3, SSE41, SSE42, F16C, POPCNT, BMI1, BMI2, PCLMUL, AES, AVX, FMA, AVX2, RDRAND, RDTSCP, XSAVE, OSXSAVE
    2024.04.22 18:27:08.680971 [ 21851 ] {} <Trace> AsynchronousMetrics: Scanning /sys/class/thermal
    2024.04.22 18:27:08.681010 [ 21851 ] {} <Trace> AsynchronousMetrics: Scanning /sys/block
    2024.04.22 18:27:08.681094 [ 21851 ] {} <Trace> AsynchronousMetrics: Scanning /sys/devices/system/edac
    2024.04.22 18:27:08.681132 [ 21851 ] {} <Trace> AsynchronousMetrics: Scanning /sys/class/hwmon
    2024.04.22 18:27:08.686872 [ 21851 ] {} <Warning> Context: Linux is not using a fast clock source. Performance can be degraded. Check /sys/devices/system/clocksource/clocksource0/current_clocksource
    2024.04.22 18:27:08.686969 [ 21851 ] {} <Warning> Context: Linux transparent hugepages are set to "always". Check /sys/kernel/mm/transparent_hugepage/enabled
    2024.04.22 18:27:08.911696 [ 21851 ] {} <Information> Application: Integrity check of the executable successfully passed (checksum: 3D80E1F632C131451BEFC024AB379208)
    2024.04.22 18:27:08.911830 [ 21851 ] {} <Trace> Application: Will do mlock to prevent executable memory from being paged out. It may take a few seconds.
    2024.04.22 18:27:08.949236 [ 21851 ] {} <Trace> Application: The memory map of clickhouse executable has been mlock'ed, total 275.15 MiB
    2024.04.22 18:27:08.949510 [ 21851 ] {} <Information> Application: Shutting down storages.
    2024.04.22 18:27:08.949536 [ 21851 ] {} <Trace> Context: Shutting down named sessions
    2024.04.22 18:27:08.949577 [ 21851 ] {} <Trace> Context: Shutting down database catalog
    2024.04.22 18:27:08.949598 [ 21851 ] {} <Trace> DatabaseCatalog: Shutting down system databases
    2024.04.22 18:27:08.949618 [ 21851 ] {} <Trace> Context: Shutting down DDLWorker
    2024.04.22 18:27:08.949635 [ 21851 ] {} <Trace> Context: Shutting down caches
    2024.04.22 18:27:08.949694 [ 21851 ] {} <Debug> Application: Shut down storages.
    2024.04.22 18:27:08.949721 [ 21851 ] {} <Debug> Application: Destroyed global context.
    2024.04.22 18:27:08.949734 [ 21851 ] {} <Information> Application: Waiting for background threads
    2024.04.22 18:27:08.949749 [ 21851 ] {} <Information> Application: Background threads finished in 0 ms
    2024.04.22 18:27:08.951056 [ 21851 ] {} <Error> Application: Code: 430. DB::Exception: Effective user of the process (root) does not match the owner of the data (clickhouse). Run under 'sudo -u clickhouse'. (MISMATCHING_USERS_FOR_PROCESS_AND_DATA), Stack trace (when copying this message, always include the lines below):

    0. DB::Exception::Exception(DB::Exception::MessageMasked&&, int, bool) @ 0x000000000cbcedbb
    1. DB::Exception::Exception<String&>(int, FormatStringHelperImpl<std::type_identity<String&>::type>, String&) @ 0x00000000076748c3
    2. DB::assertProcessUserMatchesDataOwner(String const&, std::function<void (String const&)>) @ 0x000000000cc76c7c
    3. DB::Server::main(std::vector<String, std::allocator<String>> const&) @ 0x000000000cd55e34
    4. Poco::Util::Application::run() @ 0x0000000014ca8c26
    5. DB::Server::run() @ 0x000000000cd4cf11
    6. Poco::Util::ServerApplication::run(int, char**) @ 0x0000000014cb1ad9
    7. mainEntryClickHouseServer(int, char**) @ 0x000000000cd48d0a
    8. main @ 0x0000000007658fd8
    9. /root/glibc-2.28/csu/../csu/libc-start.c:342: __libc_start_main @ 0x000000000002344b
    10. _start @ 0x0000000005deeb2e
    (version 24.3.2.23 (official build))
    2024.04.22 18:27:08.951125 [ 21851 ] {} <Information> Application: shutting down
    2024.04.22 18:27:08.951143 [ 21851 ] {} <Debug> Application: Uninitializing subsystem: Logging Subsystem
    2024.04.22 18:27:08.951299 [ 21852 ] {} <Trace> BaseDaemon: Received signal -2
    2024.04.22 18:27:08.951397 [ 21852 ] {} <Information> BaseDaemon: Stop SignalListener thread




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



tail -n 100 /var/log/clickhouse-server/clickhouse-server.log
tail -n 100 /var/log/clickhouse-server/clickhouse-server.err.log


https://juejin.cn/post/7065087471247163405
# 默认原始文件 
https://github.com/ClickHouse/ClickHouse/blob/master/programs/server/config.xml

修改完之后重启服务：
service clickhouse-server restart
systemctl start clickhouse-server


# yum 命令无反应的解决方法
## 已安装
yum list installed | grep clickhouse
## 清理yum缓存
yum clean all
## 或删除cache目录
# rm -rf /var/cache/yum/*
 
# 清理yum资源锁
rm -f /var/lib/rpm/.rpm.lock
rm -f /var/lib/rpm/.dbenv.lock

# 卸载及删除安装文件（需root权限）
yum list installed | grep clickhouse
yum remove -y clickhouse-common-static
yum remove -y clickhouse-server-common
rm -rf /var/lib/clickhouse
rm -rf /etc/clickhouse-*
rm -rf /var/log/clickhouse-server



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
sudo chown -R root:root /var/lib/clickhouse
ls -l /var/lib