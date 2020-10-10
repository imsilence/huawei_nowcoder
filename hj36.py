#encoding: utf-8

import string

def solution():
    word = input()
    plaintext = input()
    chars = []
    for ch in word.lower() + string.ascii_lowercase:
        if ch in chars:
            continue
        chars.append(ch)

    letters = ''.join(chars)
    letters += letters.upper()
    tf = dict(zip(string.ascii_letters, letters))
    rt = []
    for ch in plaintext:
        rt.append(tf.get(ch))

    print(''.join(rt))

if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            import traceback
            traceback.print_exc()
            break