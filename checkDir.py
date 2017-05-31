import os

def countFile(path):
    fileList = next(os.walk(path))[2]
    print('List of files in this directory : ')
    for item in fileList:
        print(item)

def getexFile(path,ex):
    fileList = next(os.walk(path))[2]
    print('\nList of ' + ex + ' files in this directory : ')
    exlist = []
    for item in fileList:

        name = str(item)
        if name.endswith(ex):
            print(name)
            exlist.append(item)
    return exlist

def countLines(name):
    lines = []
    with open(name, 'r') as f:
        for line in f:
            lines.append(line.rstrip())

        onlylines = []
        for line in lines:
            if line:
                onlylines.append(line)
    # for item in onlylines:
    #     print(item)
    return len(onlylines)
    # print(onlylines)

#
# path = '/home/mehulagarwal/Code/python'
# countFile(path)
#
# ex = str(input('Enter File extension (for example, enter .c for C Files) : '))
# pyfiles = getexFile(path,ex)
# print(pyfiles)
# os.chdir(path)
# count = 1
# total_len = 0
# for item in pyfiles:
#     print('\nFile ' + str(count) + ': ')
#     count = count + 1
#     total_len = total_len + countLines(item)
#
# print('\nTotal lines here : ' + str(total_len))
