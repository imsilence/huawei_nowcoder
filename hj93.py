#encoding: utf-8
'''
题目描述
编写一个函数，传入一个int型数组，返回该数组能否分成两组，使得两组中各元素加起来的和相等，并且，所有5的倍数必须在其中一个组中，所有3的倍数在另一个组中（不包括5的倍数），能满足以上条件，返回true；不满足时返回false。 
输入描述:
第一行是数据个数，第二行是输入的数据

输出描述:
返回true或者false

示例1
输入
4
1 5 -5 1
输出
true
'''
def handle(nums, diff):
    flags = [0] * len(nums)
    def incr():
        for i in range(len(flags)):
            if flags[i] == 0:
                flags[i] = 1
                break
            else:
                flags[i] = 0

    flag = lambda x : 1 if x > 0 else -1
    while sum(flags) != len(nums):
        if sum([flag(flags[i]) * nums[i] for i in range(len(nums))]) == diff:
            print(flags)
            return True
        incr()

    return False

def solution():
    input()
    nums = map(int, input().split())
    categorys = [[], [], []]
    for num in nums:
        if num % 5 == 0:
            categorys[0].append(num)
        elif num % 3 == 0:
            categorys[1].append(num)
        else:
            categorys[2].append(num)

    diff = sum(categorys[0]) - sum(categorys[1])
    if handle(categorys[2], diff):
        print(categorys)
        print("true")
    else:
        print("false")




if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            import traceback
            traceback.print_exc()
            break