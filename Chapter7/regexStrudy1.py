import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('phone Number found: ' + mo.group())
message = 'Call me at 415-555-1011 tomorrow. 415-444-999 is my office.'
mo = phoneNumRegex.search(message)
print('phone Number found: ' + mo.group())
