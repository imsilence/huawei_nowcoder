#encoding: utf-8

'''
题目描述
Levenshtein 距离，又称编辑距离，指的是两个字符串之间，由一个转换成另一个所需的最少编辑操作次数。许可的编辑操作包括将一个字符替换成另一个字符，插入一个字符，删除一个字符。编辑距离的算法是首先由俄国科学家Levenshtein提出的，故又叫Levenshtein Distance。

Ex：

字符串A:abcdefg

字符串B: abcdef

通过增加或是删掉字符”g”的方式达到目的。这两种方案都需要一次操作。把这个操作所需要的次数定义为两个字符串的距离。

要求：

给定任意两个字符串，写出一个算法计算它们的编辑距离。

 

请实现如下接口

/*  功能：计算两个字符串的距离

 *  输入： 字符串A和字符串B

 *  输出：无

 *  返回：如果成功计算出字符串的距离，否则返回-1

 */

     public   static   int  calStringDistance (String charA, String  charB)

    {

        return  0;

    }  

 


输入描述:
输入两个字符串

输出描述:
得到计算结果

示例1
输入
abcdefg
abcdef
输出
1
'''

def solution():
    txtA = input()
    txtB = input()
    distance = [[0] * (len(txtA) + 1) for i in range(len(txtB) + 1)]
    for i in range(len(txtA) + 1):
        distance[0][i] = i
    for i in range(len(txtB) + 1):
        distance[i][0] = i

    for i in range(1, len(txtA) + 1):
        for j in range(1, len(txtB) + 1):
            if txtA[i-1] == txtB[j-1]:
                distance[j][i] = distance[j-1][i-1]
            else:
                distance[j][i] = min(distance[j-1][i], distance[j][i-1], distance[j-1][i-1]) + 1
    print(distance[-1][-1])

if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            import traceback
            traceback.print_exc()
            break