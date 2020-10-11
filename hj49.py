#encoding: utf-8

'''
题目描述
问题描述：有4个线程和1个公共的字符数组。线程1的功能就是向数组输出A，线程2的功能就是向字符输出B，线程3的功能就是向数组输出C，线程4的功能就是向数组输出D。要求按顺序向数组赋值ABCDABCDABCD，ABCD的个数由线程函数1的参数指定。[注：C语言选手可使用WINDOWS SDK库函数]
接口说明：
void init();  //初始化函数
void Release(); //资源释放函数
unsignedint__stdcall ThreadFun1(PVOID pM)  ; //线程函数1，传入一个int类型的指针[取值范围：1 – 250，测试用例保证]，用于初始化输出A次数，资源需要线程释放
unsignedint__stdcall ThreadFun2(PVOID pM)  ;//线程函数2，无参数传入
unsignedint__stdcall ThreadFun3(PVOID pM)  ;//线程函数3，无参数传入
Unsigned int __stdcall ThreadFunc4(PVOID pM);//线程函数4，无参数传入
char  g_write[1032]; //线程1,2,3,4按顺序向该数组赋值。不用考虑数组是否越界，测试用例保证
输入描述:
输入一个int整数

输出描述:
输出多个ABCD

示例1
输入
10
输出
ABCDABCDABCDABCDABCDABCDABCDABCDABCDABCD
'''

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