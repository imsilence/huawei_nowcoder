#encoding: utf-8
'''
题目描述
按照指定规则对输入的字符串进行处理。

详细描述：

将输入的两个字符串合并。

对合并后的字符串进行排序，要求为：下标为奇数的字符和下标为偶数的字符分别从小到大排序。这里的下标意思是字符在字符串中的位置。

对排序后的字符串进行操作，如果字符为‘0’——‘9’或者‘A’——‘F’或者‘a’——‘f’，则对他们所代表的16进制的数进行BIT倒序的操作，并转换为相应的大写字符。如字符为‘4’，为0100b，则翻转后为0010b，也就是2。转换后的字符为‘2’； 如字符为‘7’，为0111b，则翻转后为1110b，也就是e。转换后的字符为大写‘E’。


举例：输入str1为"dec"，str2为"fab"，合并为“decfab”，分别对“dca”和“efb”进行排序，排序后为“abcedf”，转换后为“5D37BF”

接口设计及说明：

/*

功能:字符串处理

输入:两个字符串,需要异常处理

输出:合并处理后的字符串，具体要求参考文档

返回:无

*/

void ProcessString(char* str1,char *str2,char * strOutput)

{

}



输入描述:
输入两个字符串

输出描述:
输出转化后的结果

示例1
输入
dec fab
输出
5D37BF
'''
def tf(ch):
    r = {
        '0' : '0', #0000 -> 0000
        '1' : '8', #0001 -> 1000
        '2' : '4', #0010 -> 0100
        '3' : 'C', #0011 -> 1100
        '4' : '2', #0100 -> 0010
        '5' : 'A', #0101-> 1010
        '6' : '6', #0110 -> 0110
        '7' : 'E', #0111 -> 1110
        '8' : '1', #1000 -> 0001
        '9' : '9', #1001 -> 1001
        'a' : '5', #1010 -> 0101
        'b' : 'D', #1011 -> 1101
        'c' : '3', #1100 -> 0011
        'd' : 'B', #1101 -> 1011
        'e' : '7', #1110 -> 0111
        'f' : 'F', #1111 -> 1111
        'A' : '5', #1010 -> 0101
        'B' : 'D', #1011 -> 1101
        'C' : '3', #1100 -> 0011
        'D' : 'B', #1101 -> 1011
        'E' : '7', #1110 -> 0111
        'F' : 'F', #1111 -> 1111
    }
    return r.get(ch, ch)

def solution(txt):
    s1, s2 = txt.split()
    chars = list(s1) + list(s2)
    odds = sorted(chars[::2])
    evens = sorted(chars[1::2])
    i = 0
    rt = []
    while i < len(odds) or i < len(evens):
        odd = odds[i] if i < len(odds) else ''
        even = evens[i] if i < len(evens) else ''
        i += 1
        rt.append(tf(odd))
        rt.append(tf(even))
    
    return ''.join(rt)


if __name__ == '__main__':
    while True:
        try:
            txt = input()
            if txt == '':
                break
            print(solution(txt))
        except Exception:
            break
