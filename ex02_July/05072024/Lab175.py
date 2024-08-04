# OS Module
# OS module use to interact with the Operating system
#  get working dir, change dir, file exist , fileName, size file, Envir
import os
import math

print(os.name) # # e.g., 'posix' for Unix/Linux - Mac
# nt - windows

# print(os.getcwd())
# print(math.pi)
#
# os.chdir("/Users/promode/PycharmProjects/Py3xATBLearning/ex02_July/")
# print(os.getcwd())

print(os.listdir("/Users/promode/PycharmProjects/Py3xATBLearning/ex02_July/"))

# os.mkdir("pramod")

# Reaf file, You want check if exist or not.

size = os.path.getsize('testdata.txt')
print(size)

if size!=0:
    print("File EXIST and has content")
else:
    print("File don't Exist, No Content")

# Get file modification time
mtime = os.path.getmtime('testdata.txt')
print(mtime)

import time
print(time.gmtime(mtime))

print(time.localtime())
















