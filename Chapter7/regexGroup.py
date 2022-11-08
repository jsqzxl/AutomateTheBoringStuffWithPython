import re

phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('phone Number found: ' + mo.group())
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))


'''用管道匹配多个分组'''
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())


'''用？实现可选匹配'''
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHaHa')
print(mo1.group())

'''贪心和非贪心匹配'''
message = 'HaHaHaHaHa'
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search(message)
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search(message)
print(mo2.group())

''' 不区分大小写的匹配'''
robocop = re.compile(r'robocop', re.I)
print(robocop.search('Robocop is part man, part machine, all cop.').group())

print(robocop.search('ROBOCOP protects the innocent.').group())

'''sub()方法替换字符串 '''
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Ali gave the secret document to Agent Bob.'))
