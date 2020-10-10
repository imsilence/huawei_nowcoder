#encoding: utf-8

from collections import defaultdict

def solution():

    n = int(input())
    for _ in range(n):
        txt = input()
        stats = defaultdict(int)
        for ch in txt.lower():
            stats[ch] += 1

        values = sorted(stats.values(), reverse=True)
        degree = 0
        currentDegree = 26
        for v in values:
            degree += v * currentDegree
            currentDegree -= 1

        print(degree)


if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            import traceback
            traceback.print_exc()
            break