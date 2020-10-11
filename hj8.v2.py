#encoding: utf-8

from collections import defaultdict

def solution():
    n = int(input())
    rs = defaultdict(int)
    for _ in range(n):
        k, v = input().split()
        rs[int(k)] += int(v)

    for k, v in rs.items():
        print('{} {}'.format(k, v))

if __name__ == '__main__':
    solution()