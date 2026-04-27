import re

# 读取文件
with open(r'C:\Users\YUKI\Desktop\那一束月光\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 为第二期添加 task 字段
second_chapter_pattern = r"(title:\s*'第二期：再见，前任'[^}]+\})"
second_task = r"\1\n                    task: '1. 与其他嘉宾一起进行游戏互动，增进彼此了解。\n2. 注意观察宋一屿的表现，思考如何与她相处。\n3. 可以尝试与其他女嘉宾交流，了解她们的故事。'"
content = re.sub(second_chapter_pattern, second_task, content, flags=re.DOTALL)

# 为第三期添加 task 字段
third_chapter_pattern = r"(title:\s*'第三期：你好，陌生人'[^}]+\})"
third_task = r"\1\n                    task: '分享你们本次的约会，等待节目组的安排。'"
content = re.sub(third_chapter_pattern, third_task, content, flags=re.DOTALL)

# 写入文件
with open(r'C:\Users\YUKI\Desktop\那一束月光\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")
