# 安装
docker run -d --name=maxkb -p 8080:8080 -v ~/.maxkb:/var/lib/postgresql/data 1panel/maxkb

# 登录
本地登錄地址：http://localhost:8080/ui/application
用戶名: admin
密碼: MaxKB@123..

# 参考
https://rd.coach/maxkb-ai-database/

# 配置
Ollama和vLLM这两款目前比较常用的模型推理框架