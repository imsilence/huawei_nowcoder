#encoding: utf-8

'''
题目描述
给定一个正整数N代表火车数量，0<N<10，接下来输入火车入站的序列，一共N辆火车，每辆火车以数字1-9编号，火车站只有一个方向进出，同时停靠在火车站的列车中，只有后进站的出站了，先进站的才能出站。要求以字典序排序输出火车出站的序列号。

输入描述:
有多组测试用例，每一组第一行输入一个正整数N（0<N<10），第二行包括N个正整数，范围为1到9。

输出描述:
输出以字典序从小到大排序的火车出站序列号，每个编号以空格隔开，每个输出序列换行，具体见sample。

示例1
输入
3
1 2 3
输出
1 2 3
1 3 2
2 1 3
2 3 1
3 2 1
'''

def queue_in(queue, value):
    queue.append(value)

def queue_out(queue):
    return queue.pop(0) if queue else None

def stack_in(stack, value):
    stack.append(value)

def stack_out(stack):
    return stack.pop(-1) if stack else None

def handle(rt, v):
    nrt = []
    for line in rt:
        #in
        stack = line[0][:]
        output = line[1][:]

        stack_in(stack, v)
        nrt.append([stack, output])
        #out
        stack = line[0][:]
        output = line[1][:]
        while True:
            out = stack_out(stack)
            if out is None:
                break
            queue_in(output, out)
            nstack = stack[:]
            noutput = output[:]
            stack_in(nstack, v)
            nrt.append([nstack, noutput])

    return nrt

def solution():
    input()
    queue = input().split()
    rt = [[[], []]]
    while True:
        v = queue_out(queue)
        if v is None:
            break
        rt = handle(rt, v)
        # print(rt)
    for stack, output in rt:
        if not output:
            continue
        outputs = []
        while True:
            out = queue_out(output)
            if out is None:
                break
            outputs.append(out)
        while True:
            out = stack_out(stack)
            if out is None:
                break
            outputs.append(out)
        if outputs:
            print(' '.join(outputs))

if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            print(e)
            break