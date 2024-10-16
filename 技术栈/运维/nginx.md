# 参考
    通过以下 docker-compose 可秒级验证 nginx 配置，无疑是学习 nginx 的绝佳利器。

    https://www.cnblogs.com/jason2018524/p/16966083.html


# 简单安装
    docker run -d --name=nginx -p 8111:8080 nginx:latest

# 挂载目录并安装

    docker cp nginx:/etc/nginx/nginx.conf /data/docker/nginx/opt/docker_data/nginx/nginx.conf 
    docker cp nginx:/etc/nginx/conf.d /data/docker/nginx/opt/docker_data/nginx/conf.d
    docker cp nginx:/usr/share/nginx/html/ /data/docker/nginx/opt/docker_data/nginx/html
    docker cp nginx:/var/log/nginx/ /data/docker/nginx/opt/docker_data/nginx/logs

    从已经创建的nginx容器拷贝目录到宿主机指定的目录，然后重新创建容器与宿主机做映射。
    注意：挂载目录之后，在nginx配置文件配置静态目录位置时要注意使用容器内部的目录，如：/usr/share/nginx/html，不是使用/opt/docker_data/nginx/html目录。

# 启动
docker run -d \
--name=nginx1 \
-p 80:80 \
--privileged=true \
-v /data/docker/nginx/opt/docker_data/nginx/nginx.conf:/etc/nginx/nginx.conf \
-v /data/docker/nginx/opt/docker_data/nginx/conf.d:/etc/nginx/conf.d \
-v /data/docker/nginx/opt/docker_data/nginx/html/:/usr/share/nginx/html \
-v /data/docker/nginx/opt/docker_data/nginx/logs/:/var/log/nginx/ \
-v /data/docker/nginx/opt/docker_data/nginx/conf:/etc/nginx/conf \
-e TZ=Asia/Shanghai \
--add-host="host.docker.internal:host-gateway" \
nginx:latest


-v /data/docker/nginx/opt/docker_data/nginx/conf:/etc/nginx/conf \

## 说明
    docker run：运行并启动容器
    -d：在后台运行容器，并输出容器ID
    --name：设置容器的名称
    -p 8111:80：容器的80端口映射宿主机8111端口（程序访问端口）
    --privileged=true：可选配置，目录映射时避免出现权限问题
    -v：设置"宿主机目录:容器目录"映射位置
    -e：设置时区
    执行安装的镜像信息，格式：名称:标签（REPOSITORY:TAG） 

# 访问
    http://localhost:8111/



# 常用命令
nginx -T
该命令会显示 Nginx 当前正在使用的配置文件的完整内容。