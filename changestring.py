# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:50:02 2019

@author: ngochung
"""
import string
string.hexdigits
string.ascii_uppercase
replacements=(('A','4'),('E','3'),('G','6'),('I','1'),('O','0'),('S','5'),('Z','2'))
my_string=input('nhap chuoi o day:')      
new_string=my_string.upper()
if 1<=len(my_string)<=100:
    for old,new in replacements:
        new_string=new_string.replace(old,new)
else:
    False
print(new_string)