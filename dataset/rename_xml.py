# 定义文件夹路径
image_folder = 'JPEGImages'
label_folder = 'Annotations'
new_image_folder = 'new_image'
new_label_folder = 'new_label'

import os
import re
import shutil


# 定义文件名规律
image_pattern = r'(\w+)\.jpg'
label_pattern = r'<filename>(\w+)\.jpg</filename>'

# 遍历文件列表
for i, (image_name, label_name) in enumerate(zip(os.listdir(image_folder), os.listdir(label_folder))):
    # 匹配文件名
    image_match = re.match(image_pattern, image_name)
    label_match = re.search(label_pattern, open(os.path.join(label_folder, label_name)).read())

    # 重命名文件
    new_image_name = '{:04d}.jpg'.format(i+1)
    new_label_name = '{:04d}.xml'.format(i+1)
    while os.path.exists(os.path.join(new_image_folder, new_image_name)):
        i += 1
        new_image_name = '{:04d}.jpg'.format(i+1)
        new_label_name = '{:04d}.xml'.format(i+1)
    shutil.copy(os.path.join(image_folder, image_name), os.path.join(new_image_folder, new_image_name))
    shutil.copy(os.path.join(label_folder, label_name), os.path.join(new_label_folder, new_label_name))

    # 修改xml文件中的<filename>语句
    with open(os.path.join(new_label_folder, new_label_name), 'r') as f:
        xml_content = f.read()
    xml_content = re.sub(label_pattern, '<filename>{}</filename>'.format(new_image_name), xml_content)
    with open(os.path.join(new_label_folder, new_label_name), 'w') as f:
        f.write(xml_content)
