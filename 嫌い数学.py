# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 13:26:26 2019

@author: ngochung
"""
N=int(input('nhap N:'))
a=0
b=0
if 3<=N<=6:
    for i in range(N):
        c_i=str(input('nhap c_i'))
        if c_i=='ball':
            a+=1
            print(c_i)
        elif c_i=='strike':
            b+=1
        else:
            False
            
else:
    False
    