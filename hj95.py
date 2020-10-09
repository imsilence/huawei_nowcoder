#encoding: utf-8

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