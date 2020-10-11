#encoding: utf-8

'''
题目描述
原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001
组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。

 

的每段可以看成是一个0-255的整数，需要对IP地址进行校验

 

 

 

输入描述:
输入 
1 输入IP地址
2 输入10进制型的IP地址

输出描述:
输出
1 输出转换成10进制的IP地址
2 输出转换后的IP地址

示例1
输入
10.0.3.193
167969729
输出
167773121
10.3.3.193
'''
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