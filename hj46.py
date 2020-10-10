#encoding: utf-8

from collections import defaultdict

def solution():
    txt, n = input().split()
    n = int(n)
    rt = []
    for ch in txt:
        if n <= 0:
            break
        rt.append(ch)
        n -= len(ch.encode())

    print(''.join(rt))



if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            import traceback
            traceback.print_exc()
            break