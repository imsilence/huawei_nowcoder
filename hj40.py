#encoding: utf-8

'''
题目描述
输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数。

 

    /**
     * 统计出英文字母字符的个数。
     * 
     * @param str 需要输入的字符串
     * @return 英文字母的个数
     */
    public static int getEnglishCharCount(String str)
    {
        return 0;
    }
    
    /**
     * 统计出空格字符的个数。
     * 
     * @param str 需要输入的字符串
     * @return 空格的个数
     */
    public static int getBlankCharCount(String str)
    {
        return 0;
    }
    
    /**
     * 统计出数字字符的个数。
     * 
     * @param str 需要输入的字符串
     * @return 英文字母的个数
     */
    public static int getNumberCharCount(String str)
    {
        return 0;
    }
    
    /**
     * 统计出其它字符的个数。
     * 
     * @param str 需要输入的字符串
     * @return 英文字母的个数
     */
    public static int getOtherCharCount(String str)
    {
        return 0;
    }

 

 

输入描述:
输入一行字符串，可以有空格

输出描述:
统计其中英文字符，空格字符，数字字符，其他字符的个数

示例1
输入
1qazxsw23 edcvfr45tgbn hy67uj m,ki89ol.\\/;p0-=\\][
输出
26
3
10
12
'''

def solution(txt):
    stat = {
        'alpha' : 0,
        'digit' : 0,
        'empty' : 0,
        'other' : 0,
    }
    for ch in txt:
        if ch.isalpha():
            stat['alpha'] += 1
        elif ch.isdigit():
            stat['alpha'] += 1
        elif ch == ' ':
            stat['empty'] += 1
        else:
            stat['other'] += 1

    # print("{alpha} {empty} {digit} {other}".format(**stat))
    print(stat['alpha'])
    print(stat['empty'])
    print(stat['digit'])
    print(stat['other'])




if __name__ == '__main__':
    while True:
        try:
            txt = input()
            if txt == '':
                break
            solution(txt)
        except Exception as e:
            import traceback
            traceback.print_exc()
            break