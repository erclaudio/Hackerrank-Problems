# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:51:59 2023

@author: Claudio
"""

def swap_case(s):
    newS = []
    #s=s[1].upper()
    for i in range(len(s)):
        #newS.insert(i,s[i])
        if(s[i].islower()==True):
            newS.insert(i,s[i].upper())
        else:
            newS.insert(i,s[i].lower())
    
    
    separator = ''
    return separator.join(newS)
    
    
        
        
        
    #result=0
    return True

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)