
# 1. 练习 Single Table to Single Table
## 1.1. sql
```sql
CREATE DATABASE IF NOT EXISTS seatunnel_a;
CREATE DATABASE IF NOT EXISTS seatunnel_b;
CREATE TABLE `base_region`  (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `region_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;



```
## 1.2. 准备文件 mysql2mysql_batch.conf

## 1.3. 执行
    cd /app/apache-seatunnel-2.3.8
    ./bin/seatunnel.sh --config ./config/mysql2mysql_batch.conf

