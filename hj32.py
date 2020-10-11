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

def palindrome(txt, i, j, length):
    while i > 0 and j < length:
        if txt[i] != txt[j]:
             break
        i -= 1
        j += 1
    return j - i - 1
    
def solution(txt):
    length = len(txt)
    maxLength = 0
    for i in range(0, length):
        plen = palindrome(txt, i, i, length)
        if plen > maxLength:
            maxLength = plen
        
        plen = palindrome(txt, i, i+1, length)
        if plen > maxLength:
            maxLength = plen

    print(maxLength)


if __name__ == '__main__':
    while True:
        try:
            txt = input()
            if txt == '':
                break
            solution(txt)
        except:
            break