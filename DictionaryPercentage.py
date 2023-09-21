# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:48:35 2023

@author: Claudio
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total= "{:.2f}".format(sum(student_marks[query_name]))
    nrMarks= "{:.2f}".format(len(student_marks[query_name]))
    result ="{:.2f}".format((sum(student_marks[query_name])/(len(student_marks[query_name]))))
    print(result)
