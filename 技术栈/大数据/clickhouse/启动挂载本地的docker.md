# 下载镜像
    docker pull clickhouse/clickhouse-server
# 本地创建文件夹
    mkdir /data/docker/clickhouse
# 启动一个临时docker
    docker run --rm --name tmp --ulimit nofile=262144:262144  clickhouse/clickhouse-server

# 将临时docker配置cp到本地
    docker cp tmp:/etc/clickhouse-server/users.xml /data/docker/clickhouse/conf/users.xml
    docker cp tmp:/etc/clickhouse-server/config.xml /data/docker/clickhouse/conf/config.xml

# 停止临时docker
    docker container ps
# 删除临时dokcer

# 启动挂载本地的docker
    docker run -itd \
    --restart=always \
    --name clickhouse-server  \
    --ulimit nofile=262144:262144 \
    -p 28123:8123 -p 29000:9000 -p 29009:9009 \
    -v /data/docker/clickhouse/database:/var/lib/clickhouse:rw \
    -v /data/docker/clickhouse/conf/config.xml:/etc/clickhouse-server/config.xml \
    -v /data/docker/clickhouse/conf/users.xml:/etc/clickhouse-server/users.xml \
    -v /data/docker/clickhouse/log:/var/log/clickhouse-server:rw \
    clickhouse/clickhouse-server:latest

# 从控制台登录
    docker exec -it  clickhouse-server /bin/bash
# 安装DBeaver

# 默认用户名/密码
    默认的clickhouse启动后： 用户名：default. 密码：<空>

# 创建数据库
    CREATE DATABASE btc 
# 创建数据库

    ClickHouse表引擎到底怎么选
    https://developer.aliyun.com/article/762461

# address
```sql
CREATE TABLE address(
height Int32 ,
address String ,
p_address String ,
)
ENGINE = MergeTree()
PARTITION BY height
ORDER BY (height,address)
SETTINGS index_granularity=8192
```
# address_all
```sql
CREATE TABLE btc.address_all(
height Int32 ,
address String ,
p_address String ,
)
ENGINE = MergeTree()
ORDER BY (height,address)
SETTINGS index_granularity=8192

select count(*) from btc.address_all
```
# transaction_origin

```sql
CREATE TABLE transaction_origin(
address String
)
ENGINE = MergeTree()
ORDER BY (address)
SETTINGS index_granularity=8192

select * from transaction_origin
```

# address_in address_out

```sql
CREATE TABLE address_out(
height Int32 ,
address String
)
ENGINE = MergeTree()
ORDER BY (height,address)
SETTINGS index_granularity=8192
```

```sql
CREATE TABLE btc.transaction_address(
height Int32 ,
address String,
p_address String
)
ENGINE = MergeTree()
ORDER BY (height,address)
SETTINGS index_granularity=8192
```

# 参考
    docker 安装clickhouse 部署本地
    https://blog.csdn.net/tankpanv/article/details/121490107
