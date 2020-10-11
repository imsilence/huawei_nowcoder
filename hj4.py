#encoding: utf-8

'''
目描述
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
输入描述:
连续输入字符串(输入2次,每个字符串长度小于100)

输出描述:
输出到长度为8的新字符串数组

示例1
输入
abc
123456789
输出
abc00000
12345678
90000000
'''

def solution():
    maxCnt = 2
    maxLength = 8

    for _ in range(maxCnt):
        txt = input()
        length = len(txt)

        start = 0
        
        while start < length:
            end = start + maxLength
            if end < length:
                print(txt[start:end])
            else:
                print(txt[start:end] + '0' * (end - length))
            start += maxLength

        
if __name__ == '__main__':
    solution()