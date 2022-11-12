import pprint

if __name__ == "__main__":


    cats = [{'name':'Zophie', 'desc':'chubby'},{'name':'Pooka', 'desc': 'fluffy'}]

    print('jisenquan')
    print(cats)

    fileObj = open('myClass.py', 'w')
    fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
    fileObj.close()

    #print(pprint.pformat(fileObj))
