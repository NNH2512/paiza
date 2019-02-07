# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 09:30:08 2019

@author: ngochung
"""
N=int(input('nhap so lan N:'))
a=[]
b=0

if 3<=N<=6:
    for i in range(N):
        a[i]=str(input('ball or strike'))
        print(a[i])
else:
    False        