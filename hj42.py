#encoding: utf-8

'''
题目描述
Jessi初学英语，为了快速读出一串数字，编写程序将数字转换成英文：

如22：twenty two，123：one hundred and twenty three。

 

说明：

数字为正整数，长度不超过九位，不考虑小数，转化结果为英文小写；

输出格式为twenty two；

非法数据请返回“error”；

关键字提示：and，billion，million，thousand，hundred。

 

方法原型：public static String parse(long num) 

 

 

 

输入描述:
输入一个long型整数

输出描述:
输出相应的英文写法

示例1
输入
2356
输出
two thousand three hundred and fifty six
'''

def word(num, suffix):
    if num == 0:
        return ''

    bits = [''] * 3
    tf = [
        ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'],
        ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'],
        ['', 'one hundred', 'two hundred', 'three hundred', 'four hundred', 'five hundred', 'six hundred', 'seven hundred', 'eight hundred', 'nine hundred'],
    ]
    tenTf = 'ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
    # idx = 0
    # while num > 0:
    #     bits[idx] = tf[idx][num % 10]
    #     num //= 10
    #     idx += 1
    bits[2] = tf[2][num // 100]
    num %= 100
    if num >= 20:
        bits[1] = tf[1][num // 10]
        bits[0] = tf[0][num % 10]
    elif num >= 10:
        bits[1] = tenTf[num - 10]
    else:
        bits[0] = tf[0][num % 10]


    txt = bits[0]
    if bits[1]:
        txt = '{} {}'.format(bits[1], txt) if txt else bits[1]

    if bits[2]:
        txt = '{} and {}'.format(bits[2], txt) if txt else bits[2]

    return '{} {}'.format(txt, suffix)


def solution(txt):
    num = int(txt)
    units = ['', 'thousand', 'million', 'billion']
    idx = 0
    rt = []
    while num > 0:
        rt.append(word(num % 1000, units[idx]))
        num //= 1000
        idx += 1
    print(' '.join((list(filter(lambda x: x != '', rt)))[::-1]))

if __name__ == '__main__':
    while True:
        try:
            txt = input()
            if txt == '':
                break
            solution(txt)
        except Exception as e:
            break