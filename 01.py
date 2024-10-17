import os

def generate_html_links(directory):
    # 开始生成 <pre> 标签
    print("<pre>")
    
    # 遍历目录和子目录
    for root, _, files in os.walk(directory):
        for file in files:
            # 如果文件是 .md 扩展名
            if file.endswith(".md"):
                # 构造文件的相对路径
                file_path = os.path.relpath(os.path.join(root, file), directory)
                # 计算文件的目录深度，决定缩进
                depth = file_path.count(os.sep)
                # 去掉扩展名
                file_name = os.path.splitext(file)[0]
                # 生成 href 链接，按深度缩进
                indent = "    " * depth
                print(f'{indent}<a href="{file_path}">{file_name}</a>')
    
    # 结束 <pre> 标签
    print("</pre>")

# 运行函数，递归遍历当前目录下所有文件夹
if __name__ == "__main__":
    # 将当前目录作为根目录传入
    root_directory = os.getcwd()
    generate_html_links(root_directory)
