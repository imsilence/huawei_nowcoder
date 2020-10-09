#encoding: utf-8

import math

def solution(num):
    start = 0
    end = num
    middle = 0
    while True:
        middle = (end + start) / 2
        tmp = middle ** 3
        if math.fabs(tmp - num) <= 0.0005:
            break
        elif tmp > num:
            end = middle
        elif tmp < num:
            start = middle

    print("{:.1f}".format(middle))

if __name__ == '__main__':
    num = float(input())
    solution(num)