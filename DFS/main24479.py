"""
info - Baekjoon 24479(S2)
category - DFS
result - success
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def solution(link, ans, v):
    global cur
    ans[v] = cur
    for to_v in link[v]:
        if ans[to_v]:
            continue
        cur+=1
        solution(link, ans, to_v)

if __name__ == '__main__':
    n, m, r = map(int, input().split())
    link = [[] for _ in range(n + 1)]
    ans = [0] * (n + 1)
    cur = 1

    for _ in range(m):
        a, b = map(int, input().split())
        link[a].append(b)
        link[b].append(a)
    for lst in link:
        lst.sort()  # 오름차순 방문

    solution(link, ans, r)
    for i in ans[1:]:
        print(i)
