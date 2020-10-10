#encoding: utf-8

import threading
from queue import Queue

def solution():
    n = int(input())

    txts = []
    chars = 'BCD'

    event = threading.Event()
    event.set()

    notices = {}
    for ch in chars[:]:
        notices[ch] = Queue(1)

    def spout(ch, num, to):
        for i in range(num):
            if event.wait():
                event.clear()
                txts.append(ch)
                to.put("push")
        to.put("over")

    def bolt(ch, fr, to):
        notice = ''

        while notice != 'over':
            notice = fr.get()
            if notice != "over":
                txts.append(ch)
            if to:
                to.put(notice)
            else:
                event.set()


    ths = []
    th = threading.Thread(target=spout, args=('A', n, notices['B']))
    ths.append(th)
    for i in range(len(chars)):
        ch = chars[i]
        to = notices.get(chars[i+1]) if (i + 1) < len(chars) else None
        th = threading.Thread(target=bolt, args=(ch, notices[ch], to))
        ths.append(th)

    for th in ths:
        th.start()

    for th in ths:
        th.join()


    print(''.join(txts))


if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(e)
            break