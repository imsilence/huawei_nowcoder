#encoding: utf-8

'''
题目描述
功能: 求一个byte数字对应的二进制数字中1的最大连续数，例如3的二进制为00000011，最大连续2个1
    
输入: 一个byte型的数字
    
输出: 无
     
返回: 对应的二进制数字中1的最大连续数
输入描述:
输入一个byte数字

输出描述:
输出转成二进制之后连续1的个数

示例1
输入
3
输出
2
'''
def solution(num):
    cnt = 0
    bits = 0
    while num:
        if num % 2:
            cnt+=1
        else:
            if cnt > bits:
                bits = cnt
            cnt = 0
        num //= 2

    if cnt > bits:
        bits = cnt
    print(bits)


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