import os
import re
import shutil

# 定义文件夹路径
#folder = 'VOCdevkit/Annotations'

# 定义文件名规律
#pattern = r'<name>(Longitudinal|Transverse)</name>'

# 获取文件列表
#files = os.listdir(folder)

# 遍历文件列表
#for file in files:
    # 读取文件内容
#    with open(os.path.join(folder, file), 'r') as f:
#        content = f.read()

    # 替换字段
#    content = re.sub(pattern, '<name>crack</name>', content)

    # 保存文件
#    with open(os.path.join(folder, file), 'w') as f:
#        f.write(content)
import os
import re
import shutil

# 定义文件夹路径
folder = 'VOCdevkit/txt'

# 定义文件名规律
pattern = r'^2'

# 获取文件列表
files = os.listdir(folder)

# 遍历文件列表
for file in files:
    # 读取文件内容
    with open(os.path.join(folder, file), 'r') as f:
        content = f.read()

    # 替换字符
    content = re.sub(pattern, '0', content)

    # 保存文件
    with open(os.path.join(folder, file), 'w') as f:
        f.write(content)
