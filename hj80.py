#encoding: utf-8
'''
题目描述
题目标题：

将两个整型数组按照升序合并，并且过滤掉重复数组元素[注: 题目更新了。输出之后有换行]

详细描述：

接口说明

原型：

voidCombineBySort(int* pArray1,intiArray1Num,int* pArray2,intiArray2Num,int* pOutputArray,int* iOutputNum);

输入参数：

int* pArray1 ：整型数组1

intiArray1Num：数组1元素个数

int* pArray2 ：整型数组2

intiArray2Num：数组2元素个数

输出参数（指针指向的内存区域保证有效）：

int* pOutputArray：合并后的数组

int* iOutputNum：合并后数组元素个数

返回值：

void



输入描述:
输入说明，按下列顺序输入：
1 输入第一个数组的个数
2 输入第一个数组的数值
3 输入第二个数组的个数
4 输入第二个数组的数值

输出描述:
输出合并之后的数组

示例1
输入
3
1 2 5
4
-1 0 3 2
输出
-101235
'''
def solution():
    input()
    aList = list(map(int, input().split()))
    input()
    bList = list(map(int, input().split()))
    mergeList = list(set(aList + bList))
    mergeList.sort()
    print(''.join(map(str, mergeList)))

if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            break