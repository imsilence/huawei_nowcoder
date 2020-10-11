#encoding: utf-8

'''
题目描述
考试题目和要点：

1、中文大写金额数字前应标明“人民币”字样。中文大写金额数字应用壹、贰、叁、肆、伍、陆、柒、捌、玖、拾、佰、仟、万、亿、元、角、分、零、整等字样填写。（30分）

2、中文大写金额数字到“元”为止的，在“元”之后，应写“整字，如￥ 532.00应写成“人民币伍佰叁拾贰元整”。在”角“和”分“后面不写”整字。（30分）

3、阿拉伯数字中间有“0”时，中文大写要写“零”字，阿拉伯数字中间连续有几个“0”时，中文大写金额中间只写一个“零”字，如￥6007.14，应写成“人民币陆仟零柒元壹角肆分“。（40分）


输入描述:
输入一个double数

输出描述:
输出人民币格式

示例1
输入
151121.15
输出
人民币拾伍万壹仟壹佰贰拾壹元壹角伍分
'''
def solution(txt):
    digits, decimal = txt.split('.')
    digitsUnits = ['', '拾', '佰', '仟', '万', '亿']
    decimalUnits = ['角', '分']
    tf = {
        '0' : '零',
        '1' : '壹',
        '2' : '贰',
        '3' : '叁',
        '4' : '肆',
        '5' : '伍',
        '6' : '陆',
        '7' : '柒',
        '8' : '捌',
        '9' : '玖',
    }
    decimalWords = []
    for i, v in enumerate(decimal):
        word = tf.get(v)
        if word == '零':
            continue
        unit = '' if word == '零' else decimalUnits[i]
        decimalWords.append('{}{}'.format(word, unit))

    digitsWords = []
    for i, v in enumerate(digits[::-1]):
        word = tf.get(v)
        unit = '' if word == '零' else digitsUnits[i]
        word = '' if unit == '拾' and word == '壹' else word
        digitsWords.append('{}{}'.format(word, unit))

    words = []
    for i in range(len(digitsWords)-1, -1, -1):
        if i + 1 < len(digitsWords) and digitsWords[i] == '零' and digitsWords[i+1] == '零':
            continue

        words.append(digitsWords[i])

    if words:
        if words[-1] == '零':
            words = words[:-1]

    if words:
        words.append('元')

    if decimalWords:
        words.extend(decimalWords)
    else:
        words.append('整')
    print('人民币' + ''.join(words))


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