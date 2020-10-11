#encoding: utf-8

'''
题目描述
样例输出

输出123058789，函数返回值9

输出54761，函数返回值5

 

接口说明

函数原型：

   unsignedint Continumax(char** pOutputstr,  char* intputstr)

输入参数：
   char* intputstr  输入字符串；

输出参数：
   char** pOutputstr: 连续最长的数字串，如果连续最长的数字串的长度为0，应该返回空字符串；如果输入字符串是空，也应该返回空字符串；  

返回值：
  连续最长的数字串的长度

 

 

 

 

输入描述:
输入一个字符串。

输出描述:
输出字符串中最长的数字字符串和它的长度，中间用逗号间隔。如果有相同长度的串，则要一块儿输出（中间不间隔），但是长度还是一串的长度，与数字字符串间用逗号间隔。

示例1
输入
abcd12345ed125ss123058789
输出
123058789,9
'''

def solution():
    txt = input()
    nums = ""
    currents = []
    rts = []
    for ch in txt:
        if ch >= '0' and ch <= '9':
            currents.append(ch)
        else:
            if len(currents) > len(nums):
                rts = []
                nums = ''.join(currents)
                rts.append(nums)
            elif len(currents) == len(nums):
                rts.append(''.join(currents))

            currents = []

    if len(currents) > len(nums):
        rts = []
        nums = ''.join(currents)
        rts.append(nums)
    elif len(currents) == len(nums):
        rts.append(''.join(currents))
    print('{},{}'.format(''.join(rts), len(nums)))



if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            print(e)
            break