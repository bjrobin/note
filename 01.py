import os

def generate_html_links(directory):
    # 开始生成 <pre> 标签
    print("<pre>")
    
    # 遍历目录和子目录
    for root, dirs, files in os.walk(directory):
        # 忽略 .git 文件夹
        if '.git' in dirs:
            dirs.remove('.git')

        # 输出目录名，添加链接和特殊样式
        relative_root = os.path.relpath(root, directory)
        if relative_root != '.':
            depth = relative_root.count(os.sep)
            indent = "    " * depth
            # 生成文件夹的 href 链接
            folder_link = os.path.relpath(root, directory)
            print(f'{indent}<a href="{folder_link}"><strong>{os.path.basename(root)}</strong></a>/')
            
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
