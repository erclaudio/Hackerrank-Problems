# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:46:51 2023

@author: Claudio
"""

if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    arr.remove(max(arr))
    print(max(arr))
    
   # print(arr)