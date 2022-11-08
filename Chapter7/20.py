import pyperclip
import re


if __name__ == '__main__':

    message = '42'

    regex20 = re.compile(r'''(
    ^(\d{0,3})                # 前面的数字
    (((,\d{3})*)$)             # 带逗号的数字
    )''', re.VERBOSE)

    mo1 = regex20.search(message)
    print(mo1.group())


    message = '1,234'
    mo1 = regex20.search(message)
    print(mo1.group())

    message = '6,234,745'
    mo1 = regex20.search(message)
    print(mo1.group())

    message = '23,65'
    mo1 = regex20.search(message)
    print(mo1.group())
