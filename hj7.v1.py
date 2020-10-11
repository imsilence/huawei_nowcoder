#encoding: utf-8

'''
题目描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。

输入描述:
输入一个正浮点数值

输出描述:
输出该数值的近似整数值

示例1
输入
5.5
输出
6
'''

def solution(num):
    if num * 10 % 10 >= 5:
        print(int(num) + 1)
    else:
        print(int(num))

if __name__ == '__main__':
     while True:
        try:
            txt = input()
            if txt == '':
                break
            num = float(txt)
            solution(num)
        except Exception as e:
            import traceback
            traceback.print_exc()
            break