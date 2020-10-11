#encoding: utf-8

'''
题目描述
Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，比如像这些ABBA，ABA，A，123321，但是他们有时会在开始或结束时加入一些无关的字符以防止别国破解。比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　。因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？



输入描述:
输入一个字符串

输出描述:
返回有效密码串的最大长度

示例1
输入
ABBA
输出
4
'''

def isPalindrome(txt, start, end):
    if start == end:
        return True
    for i in range((end - start)//2 + 1):
        if txt[start + i] != txt[end - i]:
            return False
    
    return True

def solution(txt):
    length = len(txt)
    # secrects = []
    maxLength = 0
    for start in range(length):
        for end in range(length-1, start-1, -1):
            if isPalindrome(txt, start, end):
                # secrects.append(txt[start:end+1])
                secretLength = end + 1 - start
                if secretLength > maxLength:
                    maxLength = secretLength

    print(maxLength)


if __name__ == '__main__':
    while True:
        try:
            txt = input()
            if txt == '':
                break
            solution(txt)
        except Exception:
            break