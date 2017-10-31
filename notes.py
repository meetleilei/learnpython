import re


a = re.findall('[A-z]', 'leileiXINRUI!!!')
b = [i for i in 'leileiXINRUI!!!' if i.isalpha()]
assert a == b
print("That's the same!!")
