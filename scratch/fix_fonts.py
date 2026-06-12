import os
file_path = "d:/UET/Ki 2/Nhập môn CNS & AI/Portfolio/css/style.css"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("'Albert Sans', sans-serif", "'Be Vietnam Pro', sans-serif")
content = content.replace("'JetBrains Mono', monospace", "'Be Vietnam Pro', sans-serif")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
