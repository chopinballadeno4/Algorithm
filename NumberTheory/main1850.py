"""
info - Baekjoon 1850(S1)
category - NumberTheory
result - success
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def solution(a, b):
    if b == 0:
        return a
    else:
        return solution(b, a % b)

if __name__ == '__main__':
    a, b = map(int ,input().strip().split())
    print('1'*solution(a, b))
