txt = 'hello'
txt = txt.upper()
print(txt)

txt = 'HELLO'
txt = txt.lower()
print(txt)

txt = 'how old are you'
print(txt.capitalize())

txt = 'how old are you'
print(txt.title())

txt = 'hello world'
print(txt.index('l'))

text = 'giorgiiiiiiii'
count = text.count('i')
print(count)

text = 'how are you guys'
check = text.startswith('h')
print(check)

text = 'how are you guys'
check = text.endswith('s')
print(check)

x = 'sdaffeeifsdolnvsldkc'
check = x.isalpha()
print(check)

nums = '255905112'
check = nums.isdigit()
print(check)

combined = 'helloyes12321okey'
check = combined.isalnum()
print(check)

words = ['hello','friend','house','sun']
print(','.join(words))

text = ' giorgi '
print(text.strip()) 

txt = 'giorgi#is#eight#years#old'
x = txt.split('#',1)
print(x)

