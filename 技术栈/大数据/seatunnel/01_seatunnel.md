


# 1. 数据库
## 1.1. 启动命令
    docker run \
    --name mysql-seatunnel \
    -d \
    -p 3306:3306 \
    --restart unless-stopped \
    -v /Users/lhqer/MY/2024/大数据/seatunnel-zeta-server/mysql/var/log/mysql:/var/log/mysql \
    -v /Users/lhqer/MY/2024/大数据/seatunnel-zeta-server/mysql/var/lib/mysql:/var/lib/mysql \
    -v /Users/lhqer/MY/2024/大数据/seatunnel-zeta-server/mysql/etc/my.cnf:/etc/my.cnf \
    -e MYSQL_ROOT_PASSWORD=123456 \
    mysql:8.0.37



    mysql:8.0.37 --default-authentication-plugin=mysql_native_password

## 1.2. 复制配置文件
    docker cp mysql-ebpay-01:/etc/my.cnf /Users/lhqer/MY/2024/DC/大数据组/LOCAL/ebpay/mysql01/data/mysql/etc/my.cnf

## 1.3. 端口（如改变默认端口）
    [mysqld]
    port = 3306
# 2. docker-compose
## 2.1. docker-compose.yml
```yaml
services:
  zeta-server:
    image: my-base-image:latest
    container_name: zeta-server
    working_dir: /app
    volumes:
      - ./app:/app
    ports:
      - "8801:8801"
      - "5801:5801"
    command: >
      bash -c "
      printenv JAVA_HOME &&
      printenv PATH &&
      echo 'Java version:' && /usr/local/java/jdk/bin/java -version &&
      tail -f /dev/null
      "
```
docker compose up --build -d

# 3. seatunnel
## 3.1. 下载
    https://seatunnel.apache.org/download/
    wget "https://archive.apache.org/dist/seatunnel/2.3.8/apache-seatunnel-2.3.8-bin.tar.gz"
## 3.2. 解压
    cd /app
    tar -xzvf apache-seatunnel-2.3.8-bin.tar.gz
## 3.3. 安装插件
    cd /app/apache-seatunnel-2.3.8
    bin/install-plugin.sh 2.3.8
    bin/install-plugin.sh

    这个命令会 自动下载文件 connectors/plugin-mapping.properties中指定的所有Connector的Jar包，每个人可根据自己情况自行增减需要的connector依赖包。
## 3.4. 运行示例程序，至少需要
    cp plugin_config plugin_config.bak

    修改config/plugin_config
    --seatunnel-connectors--
    connector-fake
    connector-console
    --end--
    

## 3.5. 默认的repository的路径
    /root/.m2/repository/

## 3.6. 压缩
    tar -zcvf apache-seatunnel-2.3.8-bin.tar.gz apache-seatunnel-2.3.8

## 3.7. 启动seatunnel
    export SEATUNNEL_HOME=/app/apache-seatunnel-2.3.8
    export PATH=$PATH:$SEATUNNEL_HOME/bin

    cd /app/apache-seatunnel-2.3.8
    bin/seatunnel-cluster.sh -d

## 3.8. 打包
    tar -zcvf apache-seatunnel-2.3.8_.tar.gz apache-seatunnel-2.3.8
## 3.9. 时区
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
## 3.10. 验证
    /app/apache-seatunnel-2.3.8/bin/seatunnel.sh --config /app/apache-seatunnel-2.3.8/config/v2.batch.config.template

## 3.11. 重启
    yum install iproute -y
    ss -ltnp | grep :5801
    kill -9 2833

# 4. seatunnel web
## 4.1. 下载 apache-seatunnel-web-1.0.0-bin.tar.gz
    下载页面 https://seatunnel.apache.org/download/
    cd /app

    tar -zxvf apache-seatunnel-web-1.0.0-bin.tar.gz
    观察libs目录,可见支持的是2.3.3的版本
    tar -zxvf seatunnel-api-2.3.3.jar -C api

    tar -zxvf apache-seatunnel-web-1.0.2-bin.tar.gz
    观察libs目录,可见支持的是2.3.8的版本


## 4.2. 下载数据源插件
    yum install wget -y
    下载 https://seatunnel.apache.org/assets/files/download_datasource-4b79e6fafe80459590a6a0fc2865e5ac.sh
    复制到目录 apache-seatunnel-web-1.0.0-bin/bin
    改名为 download_datasource.sh
    1.0.2版本已经自带download_datasource.sh

    cp /app/download_datasource.sh /app/apache-seatunnel-web-1.0.0-bin/bin/download_datasource.sh
    cp /app/download_datasource.sh /app/apache-seatunnel-web-1.0.2-bin/bin/download_datasource.sh

    cd /app/apache-seatunnel-web-1.0.0-bin/bin
    cd /app/apache-seatunnel-web-1.0.2-bin/bin

    sh download_datasource.sh
    1.0.2 有3个失败的
    org.apache.seatunnel:datasource-console:jar:1.0.0
    org.apache.seatunnel:datasource-fakesource:jar:1.0.0
    org.apache.seatunnel:datasource-mongodb:jar:1.0.0
    如果找到，找到后拷贝到
    Copying /root/.m2/repository/org/apache/seatunnel/datasource-starrocks/1.0.0/datasource-starrocks-1.0.0.jar to /app/apache-seatunnel-web-1.0.2-bin/datasource

## 4.3. 启动报错解决办法
    报错：
    rm -rf /app/apache-seatunnel-web-1.0.0-bin/libs/datasource-hive-1.0.0.jar
    rm -rf /app/apache-seatunnel-web-1.0.0-bin/libs/datasource-hive-1.0.0.jar

    rm -rf /app/apache-seatunnel-web-1.0.2-bin/datasource/datasource-hive-1.0.0.jar
## 4.4. mysql驱动程序
    Caused by: java.lang.IllegalStateException: Cannot load driver class: com.mysql.cj.jdbc.Driver
### 4.4.1. mysql驱动
    下载 mysql驱动 mysql-connector-j-8.2.0.jar
    cp /app/mysql-connector-java-8.0.28.jar /app/apache-seatunnel-web-1.0.2-bin/libs/
### 4.4.2. 修改配置文件
    现象：
    Unknown exception. nested exception is org.apache.ibatis.exceptions.PersistenceException: ### Error querying database. Cause: org.springframework.jdbc.CannotGetJdbcConnectionException: Failed to obtain JDBC Connection; nested exception is com.mysql.cj.jdbc.exceptions.CommunicationsException: Communications link failure The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server. ### The error may exist in org/apache/seatunnel/app/dal/mapper/UserMapper.xml ### The error may involve org.apache.seatunnel.app.dal.mapper.UserMapper.selectByNameAndPasswd ### The error occurred while executing a query ### Cause: org.springframework.jdbc.CannotGetJdbcConnectionException: Failed to obtain JDBC Connection; nested exception is com.mysql.cj.jdbc.exceptions.CommunicationsException: Communications link failure The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.
    修改：apache-seatunnel-web-1.0.2-bin/conf/application.yml
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://host.docker.internal:3306/seatunnel?useSSL=false&useUnicode=true&characterEncoding=utf-8&allowMultiQueries=true&allowPublicKeyRetrieval=true
    # url: jdbc:mysql://172.22.88.27:3306/seatunnel?useSSL=false&useUnicode=true&characterEncoding=utf-8&allowMultiQueries=true&allowPublicKeyRetrieval=true
    username: root
    password: 123456

### 4.4.3. 修改配置文件
    现象：
    Unknown exception. secret key byte array cannot be null or empty.
    修改：apache-seatunnel-web-1.0.2-bin/conf/application.yml
    jwt:
    expireTime: 86400
    # please add key when deploy
    secretKey: 12345678123456781234567812345678
    algorithm: HS256
## 4.5. 执行脚本：
### 4.5.1. 执行脚本方法一
    编辑：apache-seatunnel-web-1.0.0-bin/script/seatunnel_server_env.sh
    修改如下：
    export HOSTNAME="172.22.88.27"
    export PORT="3306"
    export USERNAME="root"
    export PASSWORD="123456"
    运行：
    sh apache-seatunnel-web-1.0.2-bin/script/init_sql.sh
    sh /app/apache-seatunnel-web-1.0.2-bin/script/init_sql.sh
### 4.5.2. 执行脚本方法二：
    复制：apache-seatunnel-web-1.0.2-bin/script/seatunnel_server_mysql.sql文件的内容
    直接去客户端执行脚本
    
## 4.6. Web server failed to start. Port 8801 was already in use.
    yum install iproute -y
    ss -ltnp | grep :8801
    kill -9 2833

## 4.7. 拷贝文件 hazelcast-client.yaml
    现象
    Caused by: java.sql.SQLException: Access denied for user 'root'@'192.168.65.1' (using password: YES)
    复制：
    cp /app/apache-seatunnel-2.3.8/config/hazelcast-client.yaml /app/apache-seatunnel-web-1.0.2-bin/conf/hazelcast-client.yaml
    修改：conf/hazelcast-client.yaml
    - host.docker.internal:5801
    # - 172.22.88.27:5801
## 4.8. plugin-mapping.properties
    cp /app/apache-seatunnel-2.3.3/connectors/plugin-mapping.properties /app/apache-seatunnel-web-1.0.2-bin/conf/plugin-mapping.properties
## 4.9. 环境变量
    export SEATUNNEL_HOME=/app/apache-seatunnel-2.3.8
    export SEATUNNEL_WEB_HOME=/app/apache-seatunnel-web-1.0.2-bin
    export ST_WEB_BASEDIR_PATH=/app/apache-seatunnel-web-1.0.2-bin
    export PATH=$PATH:$SEATUNNEL_HOME/bin:$SEATUNNEL_WEB_HOME/bin
    source /etc/profile
## 4.10. 启动 SeaTunnel Web
    cd /app/apache-seatunnel-web-1.0.2-bin
    sh bin/seatunnel-backend-daemon.sh start

## 4.11. 访问
    http://127.0.0.1:8801/ui/
    admin
    admin
## 4.12. 日志
    tail -f /app/apache-seatunnel-2.3.8/logs/seatunnel-engine-server.log
    tail -f /app/apache-seatunnel-web-1.0.2-bin/logs/seatunnel.out  

# 5. 每次重启步骤
export SEATUNNEL_HOME=/app/apache-seatunnel-2.3.8
export SEATUNNEL_WEB_HOME=/app/apache-seatunnel-web-1.0.2-bin
export ST_WEB_BASEDIR_PATH=/app/apache-seatunnel-web-1.0.2-bin
export PATH=$PATH:$SEATUNNEL_HOME/bin:$SEATUNNEL_WEB_HOME/bin
source /etc/profile

echo $SEATUNNEL_HOME
echo $SEATUNNEL_WEB_HOME
echo $ST_WEB_BASEDIR_PATH
echo $PATH

cd /app/apache-seatunnel-2.3.8
bin/seatunnel-cluster.sh -d

/app/apache-seatunnel-2.3.8/bin/seatunnel.sh --config /app/apache-seatunnel-2.3.8/config/v2.batch.config.template

cd /app/apache-seatunnel-web-1.0.2-bin
sh bin/seatunnel-backend-daemon.sh start

http://127.0.0.1:8801/ui/
admin/admin

# 6. Seatunnel Web 试用

JDBC Url
jdbc:mysql://host.docker.internal:3306/?useSSL=false&useUnicode=true&characterEncoding=utf-8&allowMultiQueries=true&allowPublicKeyRetrieval=true


# 7. 参考


## 7.1. 网页
    Deployment of Apache SeaTunnel Web
    https://seatunnel.apache.org/seatunnel_web/1.0.0/deploy/
    seatunnel-web/README.md
    https://github.com/apache/seatunnel-web/blob/main/README.md
    seatunnel-web/README_CN.md
    https://github.com/apache/seatunnel-web/blob/main/README_CN.md
    seatunnel部署
    https://seatunnel.apache.org/zh-CN/docs/2.3.8/start-v2/locally/deployment/
    https://seatunnel.apache.org/docs/2.3.3/start-v2/locally/deployment/
    User Contribution: Apache SeaTunnel Web Deployment Guide
    https://apacheseatunnel.medium.com/user-contribution-apache-seatunnel-web-deployment-guide-263364dfb931
    Database didn't list Postgres after successful add datasource and green test connection
    https://github.com/apache/seatunnel/issues/6004
    github
    https://github.com/apache/seatunnel-web
    Simplifying Data Flow By Multi-Table Synchronization with Apache SeaTunnel（版本有些老）
    https://apacheseatunnel.medium.com/simplifying-data-flow-by-multi-table-synchronization-with-apache-seatunnel-e300f01d7d7b
    下载地址
    https://www.apache.org/dyn/closer.lua/seatunnel/2.3.8/apache-seatunnel-2.3.8-bin.tar.gz
    3分钟部署 SeaTunnel Zeta 单节点 Standalone 模式环境
    https://juejin.cn/post/7233982165363556409
## 7.2. tar参数
    -c	新建打包压缩文件
    -x	解压缩打包文件
    -v	在压缩/解压缩过程中，显示正在处理的文件名或目录
    -f	（压缩或解压时）指定要处理的压缩文件
    -j	通过bzip2指令压缩/解压缩文件，文件格式：* .tar.bz2
    -z	通过gzip指令压缩/解压缩文件，文件格式：*.tar.gz
    -C dir	指定压缩/解压缩的目录，若无指定，默认是当前目录
    -d	记录文件的差别
    -t	查看压缩文件中包含哪些文件或目录
    -r	添加文件到压缩文件
    —delete	从压缩文件中删除指定的文件




