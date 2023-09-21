# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:49:26 2023

@author: Claudio
"""

if __name__ == '__main__':
    N = int(input())
    l=[]
           
    for i in range (N):
        s = list(input().split())
        if s[0] == "insert":
            l.insert(int(s[1]),int(s[2]))
        if s[0]== "print":
            print(l)
        if s[0]=="remove":
            l.remove(int(s[1]))
        if s[0]=="append":
            l.append(int(s[1]))
        if s[0]=="sort":
            l.sort()
        if s[0]=="pop":
            l.pop()
        if s[0]=="reverse":
            l.reverse()
        
        
    # for n times
    # currentProgramArgs = input()
    # currentProgramArgs = currentProgramArgs.split()
    # if currentProgr... [0] == insert
    # insert into array, currentProgramArgs[1] is value, currentProgramArgs[2] is index
    # if .... == append
    
        
        
        
    # error handling?
    # index out bounds?
