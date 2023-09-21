# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:45:32 2023

@author: Claudio
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
print([[i,j,k]for i in range (x+1) for j in range (y+1) for k in range(z+1) if i+j+k!=n])