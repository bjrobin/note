
# 参考
    https://www.cnblogs.com/JcHome/p/16475990.html
# docker pull
    docker pull wurstmeister/kafka
    docker pull wurstmeister/kafka



## docker run 

docker run -d --name kafka -p 9002:9002 -e KAFKA_BROKER_ID=0 -e KAFKA_ZOOKEEPER_CONNECT=host.docker.internal:2181/kafka -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://127.0.0.1:9002 -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9002 -v /etc/localtime:/etc/localtime --add-host="host.docker.internal:host-gateway" wurstmeister/kafka

docker run -d --name kafka -p 9002:9002 -e KAFKA_BROKER_ID=0 -e KAFKA_ZOOKEEPER_CONNECT=host.docker.internal:2181/kafka -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://host.docker.internal:9002 -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9002 -v /etc/localtime:/etc/localtime wurstmeister/kafka:2.12-2.5.0

docker run -d --restart=always --log-driver json-file --log-opt max-size=100m --log-opt max-file=2 --name kafka -p 9002:9002 -e KAFKA_BROKER_ID=0 -e KAFKA_ZOOKEEPER_CONNECT=172.16.152.136:2181/kafka -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://172.16.152.136:9002 -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9002 -v /etc/localtime:/etc/localtime wurstmeister/kafka:2.12-2.5.0

### 参数说明：
-e KAFKA_BROKER_ID=0  在kafka集群中，每个kafka都有一个BROKER_ID来区分自己
-e KAFKA_ZOOKEEPER_CONNECT=host.docker.internal:2181/kafka 配置zookeeper管理kafka的路径host.docker.internal:2181/kafka
-e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://host.docker.internal:9002  把kafka的地址端口注册给zookeeper，如果是远程访问要改成外网IP,类如Java程序访问出现无法连接。
-e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9002 配置kafka的监听端口
-v /etc/localtime:/etc/localtime 容器时间同步虚拟机的时间

# 启动zookeeper
# 启动kafka
# 进入容器
    docker exec -it kafka /bin/bash
# 查找
    find / -iname kafka-console-producer.sh
# 进入目录
    cd /opt/kafka_2.13-2.8.1/bin/
    /opt/kafka_2.13-2.8.1/bin/kafka-console-producer.sh
# 创建一个新主题（test-kafka)来存储事件
    ./kafka-topics.sh --create --topic test-kafka --bootstrap-server localhost:9002
    Created topic test-kafka.
# 显示新主题：test-kafka 的分区信息
    ./kafka-topics.sh --describe --topic test-kafka --bootstrap-server localhost:9002
# 测试消费消息：
    ./kafka-console-consumer.sh --topic test-kafka --from-beginning --bootstrap-server localhost:9002
# 测试生产消息：
    ./kafka-console-producer.sh --topic test-kafka --bootstrap-server localhost:9002

# 先看下本地Kafka是否有这个student-write topic呢？
./kafka-topics.sh --list --zookeeper host.docker.internal:2181

# xxx
./kafka-console-consumer.sh --topic student-write --from-beginning --bootstrap-server localhost:9002
