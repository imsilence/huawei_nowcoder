#encoding: utf-8

'''
题目描述
密码要求:




1.长度超过8位




2.包括大小写字母.数字.其它符号,以上四种至少三种




3.不能有相同长度大于2的子串重复





输入描述:
一组或多组长度超过2的子符串。每组占一行

输出描述:
如果符合要求输出：OK，否则输出NG

示例1
输入
021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000
输出
OK
NG
NG
OK
'''
def isWeak(password):
    if len(password) <= 8:
        return True
    
    category = [0] * 4
    for ch in password:
        if ch >= 'a' and ch <= 'z':
            category[0] = 1
        elif ch >= 'A' and ch <= 'Z':
            category[1] = 1
        elif ch >= '0' and ch <= '9':
            category[2] = 1
        else:
            category[3] = 1

    if sum(category) < 3:
        return True

    for i in range(len(password)-3):
        substr = password[i:i+3]
        if substr in password[i+3:]:
            return True
    
    return False

def solution(txt):
    return 'NG' if isWeak(txt) else 'OK'

if __name__ == '__main__':
    while True:
        try:
            txt = input()
            if txt == '':
                break
            print(solution(txt))
        except Exception:
            break