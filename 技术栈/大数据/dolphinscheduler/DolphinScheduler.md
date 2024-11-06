# 1. Docker 快速使用教程
    https://dolphinscheduler.apache.org/zh-cn/docs/3.2.2/guide/start/docker
# 2. 下载页面
    https://dolphinscheduler.apache.org/en-us/download/3.2.2

# 3. docker-compose.yml
    volumes:
      - /Users/lhqer/MY/2024/大数据/seatunnel-zeta-server/app/apache-seatunnel-2.3.8:/opt/seatunnel/apache-seatunnel-2.3.8
      - ./mysql-connector-java-8.0.28.jar:/opt/dolphinscheduler/libs/mysql-connector-java-8.0.28.jar
# 4. 使用 docker-compose 启动服务
    下载 apache-dolphinscheduler-3.2.2-src.tar.gz
    cd '/Users/lhqer/MY/2024/大数据/DolphinScheduler/apache-dolphinscheduler-3.2.2-src/deploy/docker'
    docker compose --profile all up -d
# 5. 访问
    http://localhost:12345/dolphinscheduler
    http://localhost:12345/dolphinscheduler/ui
    DolphinScheduler 默认的用户和密码分别为 admin 和 dolphinscheduler123

# 6. 数据源1
    源名称：MYSQL01
    IP主机名：host.docker.internal
    数据库名：seatunnel_a
    jdbc连接参数：{"useSSL":"false","allowPublicKeyRetrieval":"true","useUnicode":"true","characterEncoding":"utf-8","allowMultiQueries":"true"}
# 7. 数据源2
    源名称：MYSQL02
    IP主机名：host.docker.internal
    数据库名：seatunnel_b
    jdbc连接参数：{"useSSL":"false","allowPublicKeyRetrieval":"true","useUnicode":"true","characterEncoding":"utf-8","allowMultiQueries":"true"}

# 8. 安全中心-租户管理-创建租户
    操作系统租户：appuser

# 9. 安全中心-环境管理
export SEATUNNEL_HOME=/opt/seatunnel/apache-seatunnel-2.3.8
export JAVA_HOME=/opt/java/openjdk
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH

# 10. 工作流定义
```bash
env {
  # You can set flink configuration here
  execution.parallelism = 2
  job.mode = "BATCH"
}
source{
    Jdbc {
        url = "jdbc:mysql://host.docker.internal:3306/seatunnel_a"
        driver = "com.mysql.cj.jdbc.Driver"
        connection_check_timeout_sec = 100
        user = "root"
        password = "123456"
        query = """select id,region_name from base_region"""
    }
}
 
transform {
    # If you would like to get more information about how to configure seatunnel and see full list of transform plugins,
    # please go to https://seatunnel.apache.org/docs/transform/sql
}
 
sink {
  jdbc {
        url = "jdbc:mysql://host.docker.internal:3306/seatunnel_b"
        driver = "com.mysql.cj.jdbc.Driver"
        connection_check_timeout_sec = 100
        user = "root"
        password = "123456"
        query = """
            insert into base_region(id, region_name) values(?, ?)
            on duplicate key update region_name = values(region_name)
        """

  }
}
```

# 11. 其他
# 12. telnet
    apt-get update 
    apt-get install telnet -y
    telnet host.docker.internal 3306
    telnet 172.22.88.27 3306

# 13. 拷贝
docker cp docker-dolphinscheduler-api-1:/opt/dolphinscheduler/libs/dolphinscheduler-api-dev-SNAPSHOT.jar /Users/lhqer/MY/2024/大数据/DolphinScheduler/app/apache-dolphinscheduler-3.2.2-src/deploy/docker/dolphinscheduler-api-dev-SNAPSHOT.jar

# 14. 修改pom文件，编辑添加mysql 8.x的依赖。
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.28</version>
        </dependency>

# 15. 打包
jar cvf dolphinscheduler-api-dev-SNAPSHOT.jar -C dolphinscheduler-api-dev-SNAPSHOT .
# 16. 具名挂载 怎样找到 var/lib/docker/volumes
終端機執行下方指令
mac下docker實際是在vm裡又加了一層，因此需要進入vm 才能進行操作。
docker run -it --privileged --pid=host debian nsenter -t 1 -m -u -n -i sh
解決閃退問題後，會進入VM內，輸入ls，檢視當前路徑下目錄資訊。
ls /var/lib/docker/volumes/
退出：exit
# 17. 怎样重启所有服务
    docker compose --profile all restart
# 18. 貌似可以不设置
    extra_hosts:
          - host.docker.internal:host-gateway

# 19. volumes
    volumes:
      - /Users/lhqer/MY/2024/大数据/seatunnel-zeta-server/app/apache-seatunnel-2.3.8:/opt/seatunnel/apache-seatunnel-2.3.8
      - ./dolphinscheduler-api-dev-SNAPSHOT.jar:/opt/dolphinscheduler/libs/dolphinscheduler-api-dev-SNAPSHOT.jar
      - ./mysql-connector-java-8.0.28.jar:/opt/dolphinscheduler/libs/mysql-connector-java-8.0.28.jar