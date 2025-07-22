FineBI企业版部署指南
https://help.fanruan.com/finebi/doc-view-2108.html

快速入门
https://help.fanruan.com/fineops/doc-view-54.html

# macOS系统docker安装ubuntu安装FineOps运维平台

## 
    cd /Users/qushixian/MY/2025/DC/帆软BI/本地部署
## 
    docker run -dit --name fanruan_bi_ubuntu22 \
      -p 80:80 \
      -v "$(pwd):/app" \
      -v "/root/data:/root/data" \
      -v "/root/data/registry:/root/data/registry" \
      -v /var/run/docker.sock:/var/run/docker.sock \
      ubuntu:22.04 \
      /bin/bash

## 配置
打开 Docker Desktop

点击顶部「⚙️ 设置」→ 「Docker Engine」

确认 "insecure-registries" 包含：

{
  "builder": {
    "gc": {
      "defaultKeepStorage": "21GB",
      "enabled": true
    }
  },
  "experimental": false,
  "insecure-registries": [
    "192.168.1.41:5000",
    "http://192.168.1.41:5000"
  ]
}

## 
docker exec -it fanruan_bi_ubuntu22 /bin/bash
## 
docker run -dit --name fanruan_bi_ubuntu22 \
  --privileged \
  -p 80:80 \
  -v "$(pwd):/app" \
  -v "/root/data:/root/data" \
  -v "/root/data/registry:/root/data/registry" \
  -v /sys/fs/cgroup:/sys/fs/cgroup:rw \
  docker.io/jrei/systemd-ubuntu:22.04
## finekey-operation-all.tar.gz
    cd /app
    tar zxvf finekey-operation-all.tar.gz


## finekey.yaml
/Users/qushixian/MY/2025/私人/github/note/技术栈/大数据/帆软BI/Ubuntu22.md
repo:
  url: http://host.docker.internal:5000
  username: ops_sign_key
  password: 12345678
  ssl: false   # ⚠️ 必须设置为 false，表示这是一个 HTTP 的仓库
### 
repo:
  url: http://host.docker.internal:5000         #已有repo的url|Registry URL
  username: ops_sign_key    #已有repo的用户名|Registry username
  password: 12345678    #已有repo的密码|Registry password
  ssl: false     #是否有ssl设置|Repository with SSL set or not


## 时区tzdata
    apt update && apt install -y tzdata
    然后选择 Asia/Shanghai 时区。
### 重新进入
    docker restart fanruan_bi_ubuntu22
    docker exec -it fanruan_bi_ubuntu22 /bin/bash
## 安装sudo
    apt update && apt install -y sudo
    确保 root 用户可以执行 sudo
    sudo ls /

## 容器安装docker
    apt update && apt install -y docker.io
    docker --version

## 修改权限
    chmod -R 777 /root/data/registry
## max_map_count
### 容器
    echo "vm.max_map_count=262144" >> /etc/sysctl.conf
    sysctl -p
### 宿主机
    在宿主机上设置 vm.max_map_count
    sudo sysctl -w vm.max_map_count=262144
    echo "vm.max_map_count=262144" | sudo tee -a /etc/sysctl.conf
    sudo sysctl -p


##
'/Users/qushixian/Library/Group Containers/group.com.docker/settings-store.json'

## coreutils
apt update && apt install -y coreutils

## 重设密码
htpasswd -Bc /etc/docker/registry/htpasswd ops_sign_key
12345678
12345678

## 示范正确输入：
# cat > /usr/bin/pidof <<'EOF'
> #!/bin/sh
> echo 9999
> EOF
然后别忘了赋执行权限：
chmod +x /usr/bin/pidof

pidof dockerd
9999

kill -SIGHUP $(pidof dockerd)
bash: kill: (9999) - No such process

## finekey
    apt update && apt install -y curl
    mkdir -p /var/lib/docker
    mkdir -p /etc/docker
    cd /app/finekey/bin
    ./finekey




