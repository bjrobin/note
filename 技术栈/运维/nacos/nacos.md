# 运行mysql
docker run \
--name mysql \
-d \
-p 3306:3306 \
--restart unless-stopped \
-e MYSQL_ROOT_PASSWORD=12345678 \
mysql:8.0.37

# 映射my.cnf
mkdir -p /data/mysql/etc
docker cp mysql:/etc/my.cnf /Users/qushixian/MY/2025/体育/本地环境/mysql/data/my.cnf

# 修改 /data/docker/mysql/my.cnf
[mysqld]
port=3307

# 再次运行mysql
docker run \
--name mysql \
--add-host="host.docker.internal:host-gateway" \
-d \
-p 3307:3307 \
--restart unless-stopped \
-v /Users/qushixian/MY/2025/体育/本地环境/mysql/data/my.cnf:/etc/my.cnf \
-e MYSQL_ROOT_PASSWORD=12345678 \
mysql:8.0.37

# 创建数据库
create database nacos_config CHARACTER SET utf8 COLLATE utf8_general_ci;

# 执行sql
https://github.com/alibaba/nacos/blob/master/distribution/conf/mysql-schema.sql?spm=5238cd80.72a042d5.0.0.5bc0cd36v1N8N2&file=mysql-schema.sql

# 运行nacos
docker run \
--name nacos \
-d \
-p 8848:8848 \
--restart unless-stopped \
-v /Users/qushixian/MY/2025/体育/本地环境/nacos/data/logs:/home/nacos/logs \
-e MODE=standalone \
-e SPRING_DATASOURCE_PLATFORM=mysql \
-e MYSQL_SERVICE_HOST=host.docker.internal \
-e MYSQL_SERVICE_PORT=3307 \
-e MYSQL_SERVICE_DB_NAME=nacos_config \
-e MYSQL_SERVICE_USER=root \
-e MYSQL_SERVICE_PASSWORD=12345678 \
nacos/nacos-server:latest

# 参考
## 单机模式部署
https://nacos.io/docs/latest/manual/admin/deployment/deployment-standalone/?spm=5238cd80.72a042d5.0.0.5bc0cd36v1N8N2

