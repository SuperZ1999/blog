# 将英文的帖子复制一份，后缀改成.zh.md
import os
from shutil import copyfile

if __name__ == '__main__':
    path = '.\\content'
    for dir_path, dir_names, file_names in os.walk(path):
        for file_name in file_names:
            if file_name[-6:-3] == '.en':
                # 英文的全部跳过
                continue
            if not file_name[-3:] == '.md':
                # .DS_Store跳过
                continue
            if file_name == '_index.md' or file_name == '_index.zh.md':
                # index跳过
                continue
            if dir_path == '.\\content' and (
                    file_name == 'archives.md' or file_name == 'search.md' or
                    file_name == 'about.md' or file_name == 'links.md'):
                # archives、search、about、links跳过
                continue

            if file_name[-6:-3] == '.zh':
                new_file_name = file_name[:-6] + '.en' + file_name[-3:]
            else:
                new_file_name = file_name[:-3] + '.en' + file_name[-3:]

            file_path = os.path.join(dir_path, file_name)
            new_file_path = os.path.join(dir_path, new_file_name)
            copyfile(file_path, new_file_path)
            print(file_path, '--->', new_file_path)
