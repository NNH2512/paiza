# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:22:16 2019

@author: ngochung
"""
n=int(input('nhap so hang:')
for j in range(1,11):
    s_j=str(input('nhap SET ,SUB,ADD'))
        if s_j=='SET':
            i=int(input('nhap i:'))
            if i==1:
                a1=int(input('nhap a1:'))
            elif i==2:
                a2=int(input('nhap a2:'))
            else:
                False
        elif s_j=='ADD':
            a3=int(input('nhap a3(ADD):'))
            b=a1+a3
            print(a1,b)
        elif s_j=='SUB':
            a4=int(input('nhap a4(SUB):'))
            c=a1-a4
            print(a1,c)
        else:
            False