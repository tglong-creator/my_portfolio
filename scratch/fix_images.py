with open('d:/UET/Ki 2/Nhập môn CNS & AI/Portfolio/js/main.js', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('src="assets/images/', 'src="assets/')

with open('d:/UET/Ki 2/Nhập môn CNS & AI/Portfolio/js/main.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed image paths!")
