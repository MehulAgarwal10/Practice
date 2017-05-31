import os
import checkDir

def count_lines(exfiles):
    count = 0
    total_count = 0
    for item in exfiles:
        print('File ' + str(item) + ' : ')
        count = count+1
        total_count = total_count + checkDir.countLines(item)
    return total_count


def walk_and_count(path, ex):
    global total_line_count
    print('Current Path : ' + str(path))
    exfiles = checkDir.getexFile(path, ex)
    if exfiles:
        line_count = count_lines(exfiles)
        total_line_count += line_count

    print('\nCompleted all files in this directory. Moving on.. ')
    dirlist = next(os.walk(path))[1]
    if not dirlist:
        return
    else:
        for item in dirlist:
            print('Reading sub-directory : ' + str(item) + '-- ')
            if(str(item).startswith('.')):
                continue
            elif (str(item).startswith(('sys'))):
                continue
            else:
                new_path = path + "/" + str(item)
                os.chdir(new_path)
                walk_and_count(new_path, ex)



total_line_count = 0
my_path = os.getcwd()
print('Current working directory : ')
print(my_path)
# os.chdir('/home/mehulagarwal/Code/python')

# targetPath = '/home/mehulagarwal/Code/python'
targetPath = input('Specify path to start walking : ')
# targetPath = input('Enter path to start walking : ')

# dirlist = next(os.walk(targetPath))[1]
# if len(dirlist) > 0:
#     print(dirlist)

os.chdir(targetPath)
# start_list = next(os.walk(targetPath))[1]
ex = input('Enter file extension along with the . : ')
walk_and_count(targetPath, ex)
print('Total number of lines : ' + str(total_line_count))

