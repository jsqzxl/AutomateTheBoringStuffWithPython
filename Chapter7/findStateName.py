import os
import re
import pprint

if __name__ == '__main__':

    wordRegex = re.compile(r'(([a-zA-Z])+)+')

    filename = '/home/jason/program/python/AutomateTheBoringStuffWithPython/stateName.txt'
    file = open(filename)

    fileLines = file.readlines()

    capitals = {};

    for line in fileLines:
        if len(line) > 10:
            strs = line.split('，')
            stateName = ''
            for groups in wordRegex.findall(strs[0]):
                stateName = ' '.join([stateName, groups[0]])
            #print(stateName)
            stateCapi = ''
            for groups in wordRegex.findall(strs[1]):
                stateCapi = ' '.join([stateCapi, groups[0]])
            #print(stateCapi)
            capitals[stateName] = stateCapi
    file.close()

    fileObj = open('americaCapitals.py', 'w')
    fileObj.write('capitals = ' + pprint.pformat(capitals) + '\n')
    fileObj.close()
