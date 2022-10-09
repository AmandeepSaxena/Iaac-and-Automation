import os
file = "E:\\test\\test.txt"
size = os.stat(file).st_size
print(f' {size/1000000} MBs')