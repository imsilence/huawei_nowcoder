#encoding: utf-8

import math

def solution(txt):
    rt = []
    for i in range(len(txt)-1, -1, -1):
        if txt[i] not in rt:
            rt.append(txt[i])

    print(''.join(rt))


if __name__ == '__main__':
    txt = input()
    solution(txt)