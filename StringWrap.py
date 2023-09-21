# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:56:35 2023

@author: Claudio
"""
import textwrap

def wrap(string, max_width):
  return "\n".join((textwrap.wrap(string,max_width)))



if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)