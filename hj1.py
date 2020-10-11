#encoding: utf-8

'''
题目描述
计算字符串最后一个单词的长度，单词以空格隔开。
输入描述:
一行字符串，非空，长度小于5000。

输出描述:
整数N，最后一个单词的长度。

示例1
输入
hello world
输出
5
'''

def lastWordCount(text):
    cnt = 0
    for index in range(-1, -len(text)-1, -1):
        if text[index] == ' ':
            break
        cnt += 1
    
    return cnt

def solution():
    print(lastWordCount(input()))

if __name__ == '__main__':
    print(solution())