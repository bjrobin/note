# docker安装FineOps运维平台
    cd /Users/qushixian/MY/2025/DC/帆软BI/本地部署
    --privileged 在 macOS 上不支持
    docker run -dit --name fanruan_bi_centos7 --privileged  --pid=host --user root -p 80:80 -v .:/app -v $(pwd)/data:/root/data centos:7
    指定 sysctl 选项
    docker run -dit --name fanruan_bi_centos7 --sysctl vm.max_map_count=262144 -p 80:80 -v $(pwd):/app -v $(pwd)/data:/root/data centos:7


    cd /etc/yum.repos.d/
    mv CentOS-Base.repo CentOS-Base.repo.bak
    curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

    yum clean all
    yum makecache
    yum install -y sudo


    cd /app
    tar zxvf finekey-operation-all.tar.gz

touch /etc/sysctl.conf
echo "vm.max_map_count=262144" >> /etc/sysctl.conf
sysctl -p
docker restart fanruan_bi_centos7

从控制台进入（decker desktop重启没反应）
docker exec -it fanruan_bi_centos7 /bin/bash 

yum install -y which

    cd /app/finekey/bin
    ./finekey
    在 Docker 的 Linux VM 里执行：
    sysctl -w vm.max_map_count=262144
    
    修改后，所有 Docker 容器都能继承这个值。
    重启你的容器
    docker restart fanruan_bi_centos7


dockerd &

chmod 666 /var/run/docker.sock
docker info



    java -version
如果没有安装 Java，可以安装：
bash
复制
编辑
yum install -y java-1.8.0-openjdk


docker run --name mysql -e MYSQL_ROOT_PASSWORD=123456 -d -p 3306:3306 mysql:5.7
然后修改 finekey 配置文件，连接 MySQL。