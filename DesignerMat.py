# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:15:37 2023

@author: Claudio
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
inp = input()
size = inp.split(" ")
height = int(size[0])
width = int(size[1])
mat = []
dash = '-'
combo = ".|." 

def create_line(width, level):
    pattern = []
    combo = []
    for i in range(level+level-1):
        combo.append(".|.")
    new_combo="".join(map(str, combo))
    pattern.append(new_combo)

    for i in range((width-(level+level-1)*3)//2):
        pattern.append("-")
        pattern.insert(0,"-")
    pattern = "".join(map(str, pattern))
    return pattern
def welcome(height):
    pattern=[]
    for i in range(height*3):
        if i == ((height*3)-7)//2:
            pattern.append("WELCOME")
            
        else:
            pattern.append("-")
    
    
    pattern=pattern[:height*3-6]
    pattern= "".join(map(str,pattern))
    return pattern
def create(height, width):
    for i in range((height)//2):
        level = i+1
        mat.append(create_line(width, level))
        mat.append("\n")
    mat.append(welcome(height))
    mat.append("\n")
    for i in range((height)//2):
        level = height//2-i
        mat.append(create_line(width,level))
        mat.append("\n")
    

        
create(height,width) 
mat.pop()
mat = "".join(map(str,mat))
print(mat)