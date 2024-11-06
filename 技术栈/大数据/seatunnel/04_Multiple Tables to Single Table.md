# 1. 练习 Multiple Tables to Single Table
## 1.1. sql
```sql
-- dw Source table 1
CREATE TABLE IF NOT EXISTS ads_device_switch_performance (
  `event_time` timestamp COMMENT 'Business Time',
  `device_id` VARCHAR(32) COMMENT 'Equipment id',
  `device_type` VARCHAR(32) COMMENT 'Equipment Type',
  `device_name` VARCHAR(128) COMMENT 'Equipment Name',
  `cpu_usage` INT COMMENT 'CPU Usage Rate'
) ;
 
INSERT INTO `ads_device_switch_performance` VALUES ('2024-01-15 14:25:11', '2001', '2', 'Exchanger 1', 49);
INSERT INTO `ads_device_switch_performance` VALUES ('2024-01-17 22:25:40', '2002', '1', 'Exchanger 2', 65);
 
-- dw Source table 2
CREATE TABLE IF NOT EXISTS ads_device_router_performance (
  `event_time` timestamp COMMENT 'Business Time',
  `device_id` VARCHAR(32) COMMENT 'Equipment id',
  `device_type` VARCHAR(32) COMMENT 'Equipment Type',
  `device_name` VARCHAR(128) COMMENT 'Equipment Name',
  `cpu_usage` INT COMMENT 'CPU Usage Rate'
);
 
INSERT INTO `ads_device_router_performance` VALUES ('2024-01-17 21:23:22', '1001', '1', 'Router 1', 35);
INSERT INTO `ads_device_router_performance` VALUES ('2024-01-16 17:23:53', '1002', '2', 'Router 2', 46);


-- olap Target table
CREATE TABLE `device_performance` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT 'Table Primary Key',
  `event_time` VARCHAR(32) NOT NULL COMMENT 'Business Time',
  `device_id` VARCHAR(32) COMMENT 'Equipment id',
  `device_type` VARCHAR(32) COMMENT 'Equipment Type',
  `device_name` VARCHAR(128) NOT NULL COMMENT 'Equipment Name',
  `cpu_usage` FLOAT NOT NULL COMMENT 'CPU Usage Rate Unit %',
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Create time',
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Update time',
  PRIMARY KEY (`id`)
) COMMENT='Equipment status';

```
## 1.2. 准备文件 mysql2mysql_n1_batch.conf
## 1.3. 执行
    cd /app/apache-seatunnel-2.3.8
    ./bin/seatunnel.sh --config ./config/mysql2mysql_n1_batch.conf