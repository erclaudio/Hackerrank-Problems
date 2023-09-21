# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:50:03 2023

@author: Claudio
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    t = tuple(integer_list)    
    output = hash(t)
    print(output)