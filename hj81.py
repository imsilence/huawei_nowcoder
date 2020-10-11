#encoding: utf-8
'''
题目描述
题目标题：

判断短字符串中的所有字符是否在长字符串中全部出现

详细描述：

接口说明

原型：

boolIsAllCharExist(char* pShortString,char* pLongString);

输入参数：

    char* pShortString：短字符串

    char* pLongString：长字符串

 

 

 

 

输入描述:
输入两个字符串。第一个为短字符，第二个为长字符。

输出描述:
返回值：

示例1
输入
bc
abc
输出
true
'''
def solution():
    t1 = input()
    t2 = input()
    print('false' if set(t1) - set(t2) else 'true')

if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            break