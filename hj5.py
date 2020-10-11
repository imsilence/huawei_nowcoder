#encoding: utf-8


'''
题目描述
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。（多组同时输入 ）

输入描述:
输入一个十六进制的数值字符串。

输出描述:
输出该数值的十进制字符串。

示例1
输入
0xA
输出
10
'''
def solution():
    tl = {
        '0' : 0,
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
        'a' : 10,
        'A' : 10,
        'b' : 11,
        'B' : 11,
        'c' : 12,
        'C' : 12,
        'd' : 13,
        'D' : 13,
        'e' : 14,
        'E' : 14,
        'f' : 15,
        'F' : 15,
    }

    base = 16
    b64str = ''
    while True:
        try:
            b64str = input()
        except:
            break
        b10num = 0
        for c in b64str[2:]:
            b10num = b10num * base + tl.get(c, 0)
        print(b10num)

if __name__ == '__main__':
    solution()