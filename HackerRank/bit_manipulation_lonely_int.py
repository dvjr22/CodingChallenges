#!/bin/python3

import sys

def lonely_integer(a):
    
    xor = 0
    for i in a:
        
        xor = xor ^ i
    
    return xor
    

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
