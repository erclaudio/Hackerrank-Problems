# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:55:20 2023

@author: Claudio
"""

def count_substring(string, sub_string):
    temp_string= []
    counter = 0 
    for i in range((len(string)-len(sub_string))+1):
        temp_string= []   
        for n in range(len(sub_string)):
            temp_string.insert(n,string[n])
        new_temp_string=''.join(temp_string) 
        string = string[1:]
        #print(new_temp_string,"and",sub_string)
        if(new_temp_string == sub_string):
            counter+=1 
       
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)