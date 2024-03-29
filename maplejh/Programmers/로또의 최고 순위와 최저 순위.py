# https://school.programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    match = 0
    zeros = 0
    for l in lottos:
        if not l:
            zeros += 1
        elif l in win_nums:
            match += 1
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    return [rank[match + zeros], rank[match]]
