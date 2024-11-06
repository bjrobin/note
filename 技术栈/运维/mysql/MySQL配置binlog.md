    要启用 MySQL 的 binlog（Binary Log）以支持实时数据同步，可以按照以下步骤进行配置。
    binlog 是 MySQL 的二进制日志，用于记录数据库中的更改，适用于实时数据复制、恢复等场景。

# 修改 MySQL 配置文件
    找到 MySQL 的配置文件 my.cnf（通常位于 /etc/mysql/my.cnf、/etc/my.cnf 或其他路径中）。
    然后按照以下步骤进行配置：
    在配置文件中添加或修改以下参数：

```ini
[mysqld]
# 启用 binlog
log_bin = mysql-bin
# 设置唯一的服务器 ID，每个主从服务器都需要唯一的 ID
server_id = 1
# 设置 binlog 格式
binlog_format = ROW
# 设置 binlog 保留时间（单位：天，可根据需要调整）
expire_logs_days = 7
# 可选：控制 binlog 文件大小，超过该大小会自动生成新文件
max_binlog_size = 100M
# 如果需要保证数据一致性，可以启用下述参数（影响性能）
sync_binlog = 1
```

## 参数解释
    log_bin：启用 binlog 功能。
    server_id：服务器唯一 ID，主从架构下的每台服务器必须设置不同的 ID。
    binlog_format：设置 binlog 的记录格式，推荐使用 ROW 格式以便更详细地记录每行的更改信息。CDC 等实时同步工具通常要求 ROW 格式。
    expire_logs_days：binlog 的自动清理周期，以避免磁盘空间占用过多。
    max_binlog_size：设置每个 binlog 文件的最大大小。
    sync_binlog：设置 binlog 的同步频率，sync_binlog=1 表示每次提交后立即同步到磁盘，确保数据安全（但可能影响性能）。
# 重启 MySQL 服务
    修改完配置文件后，重启 MySQL 服务以应用更改。使用以下命令（取决于系统的服务管理工具）：

## 使用 systemctl 重启（常见于 CentOS 7 及之后的版本、Ubuntu 等）
    sudo systemctl restart mysql

## 或者使用 service 命令
    sudo service mysql restart
# 检查 binlog 是否启用
    重启后，登录 MySQL 并检查 binlog 是否正常启用：
    SHOW VARIABLES LIKE 'log_bin';
    SHOW VARIABLES LIKE 'binlog_format';
    输出中应显示 log_bin=ON 且 binlog_format=ROW，表示 binlog 已成功启用并使用行级格式。
# 设置用户权限（用于数据同步）
    确保用于数据同步的用户具有读取 binlog 的权限。以下命令授予用户 REPLICATION SLAVE 和 REPLICATION CLIENT 权限：
    GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'your_user'@'host' IDENTIFIED BY 'your_password';
    FLUSH PRIVILEGES;
    要为已经存在的 root 用户授予 REPLICATION SLAVE 和 REPLICATION CLIENT 权限
    GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'root'@'%';
    FLUSH PRIVILEGES;
# 验证 binlog 的生成
    可以通过以下命令验证 binlog 是否正在生成：
    SHOW BINARY LOGS;
    此命令会列出当前生成的 binlog 文件。

    配置完成后，MySQL 将记录所有数据变更，这样 SeaTunnel 等工具就可以使用 CDC 功能读取 MySQL 的 binlog 实现实时数据同步。