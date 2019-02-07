# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:46:39 2019

@author: ngochung
"""
N=int(input())
a=0
for i in range(N):
    Q_i=int(input())
    for x in range(1,Q_i):
        if Q_i%x==0:
            a+=x
        else:
            False
    if a==(Q_i):
        print('perfect')
        print(a)
    elif (Q_i-a)==1:
        print('nearly')
        print(a)
    else:
        print('neither')
        print(a)
