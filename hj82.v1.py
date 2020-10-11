#encoding: utf-8

'''
题目描述
分子为1的分数称为埃及分数。现输入一个真分数(分子比分母小的分数，叫做真分数)，请将该分数分解为埃及分数。如：8/11 = 1/2+1/5+1/55+1/110。


接口说明

/*
功能: 将分数分解为埃及分数序列
输入参数：
String pcRealFraction:真分数(格式“8/11”)
返回值：
String pcEgpytFraction:分解后的埃及分数序列(格式“1/2+1/5+1/55+1/100”)
*/

public static String  ConvertRealFractToEgpytFract(String pcRealFraction)
{
return null;
}

如有多个解，输出任意一个



输入描述:
输入一个真分数，String型

输出描述:
输出分解后的string

示例1
输入
复制
8/11
输出
复制
1/2+1/5+1/55+1/110

'''

def solution(txt):
    n1, n2 = list(map(int, txt.split('/')))
    rt = []
    m = 2
    while n1 != 0:
        tmp = n1 * m - n2
        if tmp < 0:
            m += 1
            continue
        
        n2 = n2 * m
        n1 = tmp
        rt.append(m)
        m += 1
        
    print('+'.join(['1/{}'.format(node) for node in rt]))

if __name__ == '__main__':
    while True:
        try:
            txt = input()
            if txt == '':
                break
            solution(txt)
        except:
            break