# # https://school.programmers.co.kr/learn/courses/30/lessons/81304
'''
from collections import defaultdict
import heapq
from copy import deepcopy


def solution(n, start, end, roads, traps):
    board = defaultdict(list)
    for p, q, s in sorted(roads):
        board[p].append((q, s, 0))
        if q in traps or p in traps:
            board[q].append((p, s, 1))
    trap = dict()
    for t in range(len(traps)):
        trap[traps[t]] = t
    q = [(0, start, [0] * len(traps))]
    while q:
        cost, x, visited = heapq.heappop(q)
        if x == end:
            print(cost)
            return cost
        flag = 0
        if x in trap.keys():
            flag = visited[trap[x]]
        for nx, nc, d in board[x]:
            if nx in trap.keys():
                if (flag + visited[trap[nx]]) % 2 != d:
                    continue
                tmp = deepcopy(visited)
                tmp[trap[nx]] += 1
                heapq.heappush(q, (cost + nc, nx, tmp))
            else:
                if flag % 2 != d:
                    continue
                heapq.heappush(q, (cost + nc, nx, visited))
'''


# 5번 시간초과 -> visited를 개선(deepcopy안쓰는 방향으로) -> 다익스트라 + 비트마스킹

# 다익스트라
from collections import defaultdict
import heapq


def solution(n, start, end, roads, traps):
    board = defaultdict(list)
    for p, q, s in sorted(roads):
        board[p].append((q, s, 0))
        if q in traps or p in traps:
            board[q].append((p, s, 1))
    dist = [[1e9] * (2 ** len(traps)) for _ in range(n + 1)]
    trap = dict()
    for t in range(len(traps)):
        trap[traps[t]] = t
    q = [(0, start, 0)]
    while q:
        cost, x, state = heapq.heappop(q)
        if dist[x][state] < cost:
            continue
        flag = 0
        if x in trap.keys():
            if state & (1 << trap[x]) == (1 << trap[x]):
                flag = 1
        for nx, nc, d in board[x]:
            if nx in trap.keys():
                if state & (1 << trap[nx]) == (1 << trap[nx]):
                    if flag ^ 1 != d:
                        continue
                else:
                    if flag ^ 0 != d:
                        continue
                state = state ^ (1 << trap[nx])
                if dist[nx][state] > cost + nc:
                    dist[nx][state] = cost + nc
                    heapq.heappush(q, (cost + nc, nx, state))
            else:
                if flag != d:
                    continue
                if dist[nx][state] > cost + nc:
                    dist[nx][state] = cost + nc
                    heapq.heappush(q, (cost + nc, nx, state))
    return min(dist[end])
