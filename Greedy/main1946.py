"""
info - Baekjoon 1946(S1)
category - Greedy
result - fail
"""

import sys
input = sys.stdin.readline

def solution(N, scoreBoard):
    scoreBoard.sort(key=lambda x : x[0])
    answer = 0
    for i in range(N):
        exam = scoreBoard[i][1]
        for j in range(i-1, -1, -1):
            if exam > scoreBoard[j][1]:
                break
            if j == 0:
                answer = answer + 1

    print(answer+1)

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        scoreBoard = []
        for _ in range(N):
            scoreBoard.append(list(map(int, input().split())))
        solution(N, scoreBoard)
