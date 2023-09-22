# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:54:22 2023

@author: Claudio
"""

def mutate_string(string, position, character):
    arr = list(string)
    #print(arr)
    arr.pop(position)
    #print(arr)
    arr.insert(position, character)
    #print(arr)
    result = ''.join(arr)
        
        
    return result

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
