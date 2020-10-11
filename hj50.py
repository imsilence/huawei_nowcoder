#encoding: utf-8

'''
题目描述
请实现如下接口

    /* 功能：四则运算

     * 输入：strExpression：字符串格式的算术表达式，如: "3+2*{1+2*[-4/(8-6)+7]}"

         * 返回：算术表达式的计算结果

     */

    public static int calculate(String strExpression)

    {

        /* 请实现*/

        return 0;

    } 

约束：

pucExpression字符串中的有效字符包括[‘0’-‘9’],‘+’,‘-’, ‘*’,‘/’ ,‘(’， ‘)’,‘[’, ‘]’,‘{’ ,‘}’。

pucExpression算术表达式的有效性由调用者保证; 

 



输入描述:
输入一个算术表达式

输出描述:
得到计算结果

示例1
输入
3+2*{1+2*[-4/(8-6)+7]}
输出
25
'''
class Stack:
    def __init__(self):
        self._values = []

    def top(self):
        return None if self.empty() else  self._values[-1]

    def push(self, value):
        self._values.append(value)

    def pop(self):
        return None if self.empty() else self._values.pop(-1)

    def empty(self):
        return len(self._values) == 0

    def __str__(self):
        return ','.join(map(str, self._values))

def priority(op1, op2):
    opsPriority = {
        '+' : 1,
        '-' : 1,
        '*' : 10,
        '/' : 10,
        '(' : 0,
        '[' : 0,
        '{' : 0,
        ')' : 100,
        ']' : 100,
        '}' : 100,
    }
    return opsPriority.get(op1, 0) > opsPriority.get(op2, 0)

def solution(txt):
    nums = Stack()
    ops = Stack()
    chs = []
    callbacks = {
        '+' : lambda x, y: x + y,
        '-' : lambda x, y: x - y,
        '*' : lambda x, y: x * y,
        '/' : lambda x, y: x // y,
    }
    prev = ''
    for ch in txt:
        if ch <= '9' and ch >= '0':
            chs.append(ch)
        else:
            if chs:
                nums.push(int(''.join(chs)))
                chs = []
            elif ch == '-' and prev not in [')', ']', '}']:
                chs.append(ch)
                continue
            prev = ch

            if ops.empty():
                ops.push(ch)
            elif ch in ['(', '[', '{']:
                ops.push(ch)
            elif ch in [')', ']', '}']:
                while True:
                    op = ops.pop()
                    right = nums.pop()
                    left = nums.pop()
                    nums.push(callbacks[op](left, right))
                    if ops.top() in ['(', '[', '{']:
                        ops.pop()
                        break

                    if not priority(ch, ops.top()):
                        break

            elif priority(ch, ops.top()):
                ops.push(ch)
            else:
                while True:
                    op = ops.pop()
                    if op is None:
                        break
                    right = nums.pop()
                    left = nums.pop()
                    nums.push(callbacks[op](left, right))

                    if ops.top() in ['(', '[', '{'] or priority(ch, ops.top()):
                        break
                ops.push(ch)

    if chs:
        nums.push(int(''.join(chs)))

    while not ops.empty():
        op = ops.pop()
        right = nums.pop()
        left = nums.pop()
        nums.push(callbacks[op](left, right))

    print(nums.top())


if __name__ == '__main__':
    # solution('3+2*{1+2*[-4/(8-6)+7]}')
    # solution('3*5+8-0*3-6+0+0')
    # solution('3-10+(0+(10+5+3)-10)')

    while True:
        try:
            txt = input()
            if txt == '':
                break
            solution(txt)
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(e)
            break