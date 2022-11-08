import pyperclip
import re

if __name__ == '__main__':

    namesRegex = re.compile(r'''(
    ^(([A-Z]([a-zA-Z]*)))
    ((\s([a-zA-Z]+))*)
    (\s(Nakamoto))
    )''', re.VERBOSE)

    message = 'Sotoshi Nakamoto'
    mo1 = namesRegex.search(message)
    print(mo1.group())

    message = 'Sotoshi mo Nakamoto'
    mo1 = namesRegex.search(message)
    print(mo1.group())

    message = 'Nakamoto'
    mo1 = namesRegex.search(message)
    print(mo1.group())
