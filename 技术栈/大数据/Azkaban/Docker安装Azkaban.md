# 1
1.拉取镜像

docker pull gayakwad/azkaban-solo:3.40.0

2.打tag

docker tag gayakwad/azkaban-solo:3.40.0 azkaban-solo:3.40.0

3.启动

docker run -ti -p 8081:8081 azkaban-solo:3.40.0

4.浏览器访问http://azkaban-solo所在主机IP地址:8081/，用户名、密码都是azkaban
# 2
docker pull gayakwad/azkaban-solo
docker run  -d --name azkaban -p 8081:8081 azkaban-solo

# 检查azkaban进程
jps -l