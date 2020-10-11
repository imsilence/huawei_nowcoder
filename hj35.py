#encoding: utf-8

'''
题目描述
题目说明

蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。

 

 

 

样例输入

5

样例输出

1 3 6 10 15

2 5 9 14

4 8 13

7 12

11

接口说明

原型

void GetResult(int Num, char * pResult);

输入参数：

        int Num：输入的正整数N

输出参数：

        int * pResult：指向存放蛇形矩阵的字符串指针

        指针指向的内存区域保证有效

返回值：

        void

 

 

输入描述:
输入正整数N（N不大于100）

输出描述:
输出一个N行的蛇形矩阵。

示例1
输入
4
输出
1 3 6 10
2 5 9
4 8
7

'''

def solution(num):
    rt = [[0] * num for _ in range(num)]
    idx = 1
    for i in range(num):
        for j in range(0, i+1):
            rt[i-j][j] = idx
            idx += 1

    for line in rt:
        print(' '.join([str(x) for x in line if x != 0]))

if __name__ == '__main__':
     while True:
        try:
            txt = input()
            if txt == '':
                break
            num = int(txt)
            solution(num)
        except Exception as e:
            import traceback
            traceback.print_exc()
            break