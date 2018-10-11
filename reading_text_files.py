'''
Created on Oct 6, 2018

@author: Tanner Yilmaz
'''

import os
 
print(os.getcwd()) #directory you are currently working in
os.chdir(r'\Users\Tanner Yilmaz\Desktop') #Directory is changed to specified directory 
print(os.getcwd()) #New Directory you are working in
 
file = open('test_print_one.txt','w') #Opens a new file and overwrites all of the information in the file. 'a' will append instead of overwriting
file.write('hello world, you are funny')
file.close()
 
file = open('test_print_one.txt','r')#File contents are read and printed to console
message = file.read()
print(message)
file.close()

