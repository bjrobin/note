
# 镜像
docker pull flink
# yml
添加文件：/Users/lhqer/MY/2024/data/docker/flink/docker-compose.yml
``` yml
version: "2.1"
services:
  jobmanager:
    image: flink
    expose:
      - "6123"
    ports:
      - "8081:8081"
    command: jobmanager
    environment:
      - JOB_MANAGER_RPC_ADDRESS=jobmanager
  taskmanager:
    image: flink
    expose:
      - "6121"
      - "6122"
    depends_on:
      - jobmanager
    command: taskmanager
    links:
      - "jobmanager:jobmanager"
    environment:
      - JOB_MANAGER_RPC_ADDRESS=jobmanager
```

# 在文件夹路径下执行
docker-compose up -d
# 访问
http://127.0.0.1:8081/