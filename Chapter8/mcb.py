import shelve
import pyperclip
import sys

if __name__ == '__main__':

    fileName = 'mcb'
    mcbShelf = shelve.open(fileName)

    # Save clipboard contend.
    print(sys.argv)
    if len(sys.argv) == 3:
        if sys.argv[1].lower() == 'save':
            mcbShelf[sys.argv[2]] = pyperclip.paste()
        elif sys.argv[1].lower() == 'delete':
            mcbShelf.pop(sys.argv[2])
    elif len(sys.argv) == 2:
        # list kerwords and load content.
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcbShelf.keys())))
        elif sys.argv[1].lower() == 'delete':
            mcbShelf.clear()
        elif sys.argv[1] in mcbShelf:
            pyperclip.copy(mcbShelf[sys.argv[1]])

    mcbShelf.close()
