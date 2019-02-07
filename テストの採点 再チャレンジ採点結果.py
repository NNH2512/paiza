# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 13:26:26 2019

@author: ngochung
"""
N,M=map(int,input('nhap N, M :').split(' '))
if 1<=(N and M)<=100:
    for i in range(1,N+1):
        a_i,b_i=map(int,input('nhap a_i and b_i:').split(' '))
        if 0<=a_i<=100 and 0<=b_i<=15 and (a_i-5*b_i)>=M:
            print(i)
        else:
            False
else:
    False
