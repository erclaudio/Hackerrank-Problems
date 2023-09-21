# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:56:07 2023

@author: Claudio
"""

if __name__ == '__main__':
    s = input()
    isalnum=False
    isalpha=False
    isdigit=False
    islower=False
    isupper=False 
    
    for i in range(len(s)):
        if(s[i].isalnum()==True):
            isalnum=True
        if(s[i].isalpha()==True):
            isalpha=True
        if(s[i].isdigit()==True):
            isdigit=True
        if(s[i].islower()==True):
            islower=True
        if(s[i].isupper()==True):
            isupper=True
    
print(isalnum)
print(isalpha)
print(isdigit)
print(islower)
print(isupper)