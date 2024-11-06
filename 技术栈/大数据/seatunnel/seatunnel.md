# 1. 参考
    使用Docker进行部署
    https://seatunnel.apache.org/zh-CN/docs/start-v2/docker/
# 2. Apache SeaTunnel
    https://seatunnel.apache.org/zh-CN/docs/about/
    SeaTunnel是一个简单易用的数据集成框架，在企业中，由于开发时间或开发部门不通用，往往有多个异构的、运行在不同的软硬件平台上的信息系统同时运行。 数据集成是把不同来源、格式、特点性质的数据在逻辑上或物理上有机地集中，从而为企业提供全面的数据共享

# 3. 安装
    docker pull apache/seatunnel:2.3.8
# 4. 启动
    docker run -d --name seatunnel_master \            
    --network seatunnel-network \
    --rm \
    -p 5801:5801 \
    apache/seatunnel:2.3.8 \
    ./bin/seatunnel-cluster.sh -r master

# 5. 运行此命令获取master容器的ip
    docker inspect seatunnel_master
# 6. 启动worker节点
    将 ST_DOCKER_MEMBER_LIST 设置为master容器的ip
    docker run -d --name seatunnel_worker_1 \
        --network seatunnel-network \
        --rm \
        -e ST_DOCKER_MEMBER_LIST=172.19.0.2:5801 \
        apache/seatunnel:2.3.8 \
        ./bin/seatunnel-cluster.sh -r worker

# 7. 启动第二个worker节点
    将ST_DOCKER_MEMBER_LIST设置为master容器的ip
    docker run -d --name seatunnel_worker_2 \
        --network seatunnel-network \
        --rm \
        -e ST_DOCKER_MEMBER_LIST=172.19.0.2:5801 \
        apache/seatunnel:2.3.8 \
        ./bin/seatunnel-cluster.sh -r worker    
# 8. 查看节点的日志
    启动完成后，可以运行docker logs -f seatunnel_master, docker logs -f seatunnel_worker_1来查看节点的日志
    当你访问http://localhost:5801/hazelcast/rest/maps/system-monitoring-information 时，可以看到集群的状态为1个master节点，2个worker节点.