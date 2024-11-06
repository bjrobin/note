docker pull mysql:8.0.37
# mysql
docker run \
--name mysql \
-d \
-p 3306:3306 \
--restart unless-stopped \
-v /data/mysql/log:/var/log/mysql \
-v /data/mysql/data:/var/lib/mysql \
-v /data/mysql/conf:/etc/mysql \
-v /data/mysql/conf.d:/etc/mysql/conf.d \
-e MYSQL_ROOT_PASSWORD=12345678 \
mysql:8.0.37


# mysql1

docker run \
--name mysql1 \
-d \
-p 3306:3306 \
--restart unless-stopped \
-v /data/mysql1/data:/var/lib/mysql \
-v /data/mysql1/etc/my.cnf:/etc/my.cnf \
-e MYSQL_ROOT_PASSWORD=12345678 \
mysql:8.0.37

# 映射my.cnf
mkdir -p /data/mysql/etc
docker cp mysql:/etc/my.cnf /data/mysql/etc




# 复制文件步骤：
1、停止mysqlB。
2、移除 /var/lib/mysql 路径下除 performance_schema 文件夹的其余文件。
3、拷贝 /var/lib/mysql-old 路径下所有文件到 /var/lib/mysql，除了 performance_schema、iblogfile_0,iblogfile_1。
4、现在/var/lib/mysql下面的文件来源和作用是：
performace_schema: 新，性能监控，它在5.6及其之前的版本中，默认没有启用，从5.7及其之后的版本才修改为默认启用。
数据库目录：老，具体存储数据的目录，每个数据库对应一个文件夹，文件夹的名字和数据库的名称一致。
ibdata1: 老，用来构建innodb系统表空间的文件，这个文件包含了innodb表的元数据、undo日志、修改buffer和双写buffer。
iblogfile_0,iblogfile_1: 新，日志文件，被删除了，重启后会重新生成。
5、重启mysqlB。


# unless-stopped always区别
always 策略会在所有情况下尝试重启容器，包括手动停止后。 unless-stopped 策略尊重手动停止的决定，不会在手动停止后自动重启容器
# 技巧
没有挂载日志文件目录是因为可以使用命令docker logs ... 来查看日志
# binlog
binlog 是 MySQL 的二进制日志，用于记录数据库中的更改，适用于实时数据复制、恢复等场景。

