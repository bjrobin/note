# 部署 Docker 集群
    https://doris.apache.org/zh-CN/docs/1.2/install/construct-docker/run-docker-cluster/

# CREATE TABLE
    CREATE DATABASE db_test;
# CREATE TABLE
    CREATE TABLE example_db.table_hash
    (
        k1 TINYINT,
        k2 DECIMAL(10, 2) DEFAULT "10.5",
        k3 CHAR(10) COMMENT "string column",
        k4 INT NOT NULL DEFAULT "1" COMMENT "int column"
    )
    COMMENT "my first table"
    DISTRIBUTED BY HASH(k1) BUCKETS 32

# 报错1105
    1105 - errCode = 2, detailMessage = Failed to find 3 backends for policy: cluster|query|load|schedule|tags|medium: default_cluster|false|false|true|[{"location" : "default"}]|HDD
    这个报错主要是由于你的doris是单机部署的，be的个数不满足3个。

# CREATE TABLE
    CREATE TABLE db_test.table_hash
    (
        k1 TINYINT,
        k2 DECIMAL(10, 2) DEFAULT "10.5",
        k3 CHAR(10) COMMENT "string column",
        k4 INT NOT NULL DEFAULT "1" COMMENT "int column"
    )
    COMMENT "my first table"
    DISTRIBUTED BY HASH(k1) BUCKETS 3
    properties(
    "replication_num"="1"
    );

# SELECT
SELECT * from db_test.table_hash