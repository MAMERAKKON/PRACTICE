import string
from random import randint

code_list = list(string.ascii_letters)

code = ''
for i in range(10):
    code_list.append(str(i))
print(code_list)
with open('CODE','w') as c:
    for i in range(6):
        code += code_list[randint(0,len(code_list))]
    print(code)
    print(code_list)
    c.write(code)