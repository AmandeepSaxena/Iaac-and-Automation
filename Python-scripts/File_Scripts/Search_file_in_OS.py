import os
import platform
import string

#for platform independent use platform.system == 'Windows' and use string.ascii_uppercase to get drive names
file = 'test.txt'
drives=['C:','D:','E:']
for dri in drives:
    #enumerate id dir and files in all drives
    # r is path d is a list of directories and f is a list file in os.walk as list 
    for r,d,f in os.walk(dri):
        #now check each files in f list
        for each_f in f:
            if each_f == file:
                print("file found")
                #join path of dir and file found anf give output
                print(os.path.join(r,each_f))

'''
#for Linux
path = "/"
for d,r,f in os.walk(path):
    for each_f in f:
        if each_f == file:
            print("file found:)
            print(os.path.join(r,each_f))
'''