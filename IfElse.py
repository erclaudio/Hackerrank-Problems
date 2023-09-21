# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:41:09 2023

@author: Claudio
"""

if __name__ == '__main__':
    n = int(input().strip())

    if n%2!=0:
        print("Weird")
    if n%2==0 and n>20:
        print("Not Weird")
    if n%2==0 and n in range(6,21,1):
        print("Weird")
    if n%2==0 and n in range(2,6,1):
        print("Not Weird")