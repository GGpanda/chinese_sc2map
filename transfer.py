import re
import os

# 指定文件路径
file_path = r'E:\SC2Code\blizzard-tutorials-chinese\full_chinese.md'

# 尝试打开和读取文件
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text_block = file.read()

    # Find all translation blocks
    translation_blocks = re.findall(r'翻译 (.*?\.md)\n(.*?)(?=\n\n## 翻译|\Z)', text_block, re.DOTALL)

    for path, content in translation_blocks:
        directory = os.path.dirname(path)
        # Make sure the directory exists
        if not os.path.exists(directory):
            os.makedirs(directory)
        # Write content to file
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content.strip())

    # 打印确认信息
    print("Content has been written to the specified files.")

except FileNotFoundError:
    print(f"The file {file_path} was not found.")
except IOError as e:
    print(f"An error occurred: {e}")