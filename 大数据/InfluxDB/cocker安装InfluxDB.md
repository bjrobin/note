docker run -p 8086:8086 --name influxdb-dev influxdb:latest
用户名：root
密码：influx_pass
初始的organization（组织名称）：manager
初始的bucket名称：manager_test_bucket

organization：一组用户的工作区。一个组织可以创建很多用户、bucket、仪表板、任务。组织是最大的环境，不同组织下的数据都是隔离的。
bucket：存储桶，类似于数据库的概念。同时桶中每个数据都会有存储周期，过多长时间就会删除，或是永久保存。

通过外部工具连接时，需要token验证，token的位置在：
点击左侧的【Data】
点击右侧的【API Tokens】
然后点击【root’s Token】，就可以得到当前用户的token