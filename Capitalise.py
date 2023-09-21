# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:57:57 2023

@author: Claudio
"""
import os

def solve(s):
    #print(s.upper())
    string= [x for x in s] #add each character of the string to an array
    string[0]= string[0].upper() #convert the first letter to upper automatically
    for i in range(len(string)):
        if(string[i]==' '):
            string[(i+1)]=string[(i+1)].upper()
    string= ''.join(string)
   # print(string)
    return string
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()