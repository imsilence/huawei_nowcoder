#encoding: utf-8

'''
题目描述
请实现如下接口

public static int findNumberOf1( int num)

{

/* 请实现 */

return 0;

} 譬如：输入5 ，5的二进制为101，输出2


涉及知识点：

注意多组输入输出！！！！！！
输入描述:
输入一个整数

输出描述:
计算整数二进制中1的个数

示例1
输入
5
输出
2
'''
def solution(num):
    cnt = 0
    while num:
        if num % 2:
            cnt += 1
        num >>= 1

    print(cnt)


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