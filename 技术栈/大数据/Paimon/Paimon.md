# 1. 官网
https://paimon.apache.org/

# 2. 说明
Paimon只是一个存储引擎。它没有自己的服务，甚至没有自己的计算引擎，而是借助Flink或Spark执行。
# 3. Seatunnel产生数据
## 3.1. mysql_cdc_to_paimon.conf
```shell
env {
  parallelism = 1
  job.mode = "STREAMING"
  checkpoint.interval = 5000
}

source {
  Mysql-CDC {
    base-url = "jdbc:mysql://host.docker.internal:3306/seatunnel_a"
    username = "root"
    password = "123456"
    table-names = ["seatunnel_a.base_region"]
  }
}

transform {
}

sink {
  Paimon {
    catalog_name="seatunnel_test"
    warehouse="file:///app/paimon/data/"
    database="seatunnel_b"
    table="base_region"
  }
}
```

## 3.2. 启动任务
    /app/apache-seatunnel-2.3.8/bin/seatunnel.sh --config /app/apache-seatunnel-2.3.8/config/mysql_cdc_to_paimon.conf

# 4. starrocks-查看数据
## 4.1. 启动starrocks
    docker run -p 9030:9030 -p 8030:8030 -p 8040:8040 -v /Users/lhqer/MY/2024/大数据/seatunnel-zeta-server/app/paimon:/paimon -itd registry.starrocks.io/starrocks/allin1-ubuntu:latest
## 4.2. 创建 EXTERNAL CATALOG
```sql
CREATE EXTERNAL CATALOG paimon_catalog_3
PROPERTIES
(
    "type" = "paimon",
    "paimon.catalog.type" = "filesystem",
    "paimon.catalog.warehouse" = "file:///paimon/data"
);
SHOW CATALOGS;
SHOW DATABASES FROM paimon_catalog_3;
select * from paimon_catalog_3.seatunnel_b.base_region;
```


# 5. 编译
## 5.1. 进入 Paimon 安装目录
    cd /app/paimon-release-0.9.0
## 5.2. 安装maven
    yum install wget -y
    yum install -y zip

    下载地址：https://maven.apache.org/download.cgi
    wget apache-maven-3.9.9-bin.tar.gz
    tar -xvf apache-maven-3.9.9-bin.tar.gz
    sudo mv apache-maven-3.9.9 /opt/maven
    vi /etc/profile.d/maven.sh
    export MAVEN_HOME=/opt/maven
    export PATH=$MAVEN_HOME/bin:$PATH
    source /etc/profile.d/maven.sh

## 5.3. 编译
    mvn clean install -DskipTests