with open('論語.txt', 'r', encoding='utf-8') as f:
    content = f.read()

result = ''
for char in content:
    if char not in [' ', '\n', '\r', '\t']:
        result += char + ' '
    else:
        result += char

with open('論語_分词版.txt', 'w', encoding='utf-8') as f:
    f.write(result)

print("处理完成！")