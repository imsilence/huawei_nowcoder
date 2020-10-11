#encoding: utf-8

'''
题目描述
查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
输入描述:
输入两个字符串
输出描述:
返回重复出现的字符
示例1
输入
abcdefghijklmnop
abcsafjklmnopqrstuvw
输出
jklmnop
'''
def solution():
    txtA = input()
    txtB = input()
    maxLength = 0
    substr = []
    if len(txtA) > len(txtB):
        txtA, txtB = txtB, txtA
    for i in range(len(txtA)):
        for j in range(len(txtA)-1, i, -1):
            if j - i > maxLength and txtA[i:j] in txtB:
                substr = txtA[i:j]
                maxLength = j - i
    print(substr)

if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            import traceback
            traceback.print_exc()
            break