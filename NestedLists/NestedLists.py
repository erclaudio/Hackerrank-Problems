# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:29:21 2023

@author: Claudio
"""

if __name__ == '__main__':
    list_stud= []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_stud.insert(_,[name,score])
        scores.insert(_,score)
    list_stud.sort(key= lambda x: x[1])
    scores1 = list(dict.fromkeys(scores))
    scores1.sort()
    #print(scores1)
    result=[]
    second = scores1[1]
    for i in range(len(list_stud)):
        if second==list_stud[i][1]:
            result.insert(i,list_stud[i])
    result.sort(key = lambda x: x[0])
    for i in range(len(result)):
        print(result[i][0])

"""
Input

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
"""
