#encoding: utf-8


def encrypt(txt):
    tf = dict(zip(
        'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',
        'BCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyza1234567890'
    ))
    rt = []
    for ch in txt:
        rt.append(tf.get(ch))
    
    return ''.join(rt)

def decrypt(txt):
    tf = dict(zip(
        'BCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyza1234567890',
        'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    ))
    rt = []
    for ch in txt:
        rt.append(tf.get(ch))
    
    return ''.join(rt)

def solution():
    plaintext = input()
    ciphertext = input()
    print(encrypt(plaintext))
    print(decrypt(ciphertext))
if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            print(e)
            break