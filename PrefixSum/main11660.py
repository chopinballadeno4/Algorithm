"""
info - Baekjoon 11660(S1)
category - Prefix sum, Dynamic programming
result - fail
"""

def solution(accumGraph, graph, start, end):

if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        solution(graph, (x1,y1), (x2,y2))
