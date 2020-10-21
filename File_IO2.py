#FILE I/O

with open('test.txt', mode='r') as my_file:
    print(my_file.read())
#!!! Make sure you have the right directory/path !!!


with open('path1/path2/current_path') as my_file:
    print(my_file.read())
#!!! Add slashes and the correct pathway
#to correctly reach files !!!
