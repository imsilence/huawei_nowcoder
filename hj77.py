#encoding: utf-8

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