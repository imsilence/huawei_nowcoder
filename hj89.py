#encoding: utf-8

from itertools import product, permutations

def calc(faces, ops):
    tf = {
        'A' : 1,
        'J' : 11,
        'Q' : 12,
        'K' : 13,
    }

    callback = {
        '+' : lambda x, y: x + y,
        '-' : lambda x, y: x - y,
        '*' : lambda x, y: x * y,
        '/' : lambda x, y: x // y,
    }
    faceInt = lambda x: int(tf.get(x, x))

    rt = faceInt(faces[0])
    txts = [faces[0]]
    for i in range(len(ops)):
        rt = callback[ops[i]](rt, faceInt(faces[i+1]))
        txts.append(ops[i])
        txts.append(str(faces[i+1]))
    return rt, ''.join(txts)

def solution(txt):

    faces = txt.split()
    ops = ['+', '-', '*', '/']

    if 'joker' in faces or 'JOKER' in faces:
        print("ERROR")
    else:
        for cfaces in permutations(faces):
            for cops in product(ops, repeat=3):
                rt, txt = calc(cfaces, cops)
                if 24 == rt:
                    print(txt)
                    return

        print('NONE')

if __name__ == '__main__':
    solution(input())