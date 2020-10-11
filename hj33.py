#encoding: utf-8

from functools import reduce

def ip2int(ip):
    return reduce(lambda x, y: (x << 8) + y, map(int, ip.split('.')), 0)

def int2ip(ip10):
    rt = []
    for _ in range(4):
        rt.append(str(ip10 % 256))
        ip10 >>= 8
    return '.'.join(rt[::-1])

def solution():
    ip = input()
    ip10 = int(input())
    print(ip2int(ip))
    print(int2ip(ip10))

if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            print(e)
            break