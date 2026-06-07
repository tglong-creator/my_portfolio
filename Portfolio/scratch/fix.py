with open('d:/UET/Ki 2/Nhập môn CNS & AI/Portfolio/js/main.js', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(r'\`', '`')
# Also let's fix \lambda just in case it should be \\lambda
content = content.replace(r'\lambda', r'\\lambda')

with open('d:/UET/Ki 2/Nhập môn CNS & AI/Portfolio/js/main.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed backticks!")
