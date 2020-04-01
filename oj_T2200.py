# Script Name       : oj_T2200.py
# Author            : Styphon
# Created           : 4/1/2020
# Version           : 1.1

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
oA = 0
eB = 0
for i in A:
        if i % 2 == 1:
        oA += 1
for i in B:
    