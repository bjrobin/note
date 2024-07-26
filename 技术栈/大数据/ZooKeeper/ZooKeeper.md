https://zookeeper.apache.org/

docker pull zookeeper
docker pull wurstmeister/zookeeper

docker run  -p 2181:2181 --privileged=true  --name zookeeper  -d  zookeeper
docker run -d --name zookeeper -p 2181:2181 -v /etc/localtime:/etc/localtime zookeeper
docker run -d --name zookeeper -p 2181:2181 -v /etc/localtime:/etc/localtime zookeeper:3.6
docker run -d --restart=always --log-driver json-file --log-opt max-size=100m --log-opt max-file=2  --name zookeeper -p 2181:2181 -v /etc/localtime:/etc/localtime wurstmeister/zookeeper