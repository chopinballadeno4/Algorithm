"""
info - Baekjoon 5567(S2)
category - BFS
result - success
"""

import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**7)

def solution(n, relation):
    result = 0
    visited = [False for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    for i in relation:
        a, b = i
        graph[a].append(b)
        graph[b].append(a)

    queue = deque()
    queue.append((1,0))
    visited[1] = True

    while queue:
        val, v = queue.popleft()
        if v < 3 and v > 0:
            result = result + 1
        for i in graph[val]:
            if visited[i] == False:
                queue.append((i, v+1))
                visited[i] = True

    print(result)

if __name__ == '__main__':
    n = int(input().strip())
    m = int(input().strip())
    relation = []
    for _ in range(m):
        a, b = map(int, input().strip().split())
        relation.append((a, b))
    solution(n, relation)
