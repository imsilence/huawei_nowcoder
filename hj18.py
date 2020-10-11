#encoding: utf-8

'''
题目描述
请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。

所有的IP地址划分为 A,B,C,D,E五类

A类地址1.0.0.0~126.255.255.255;

B类地址128.0.0.0~191.255.255.255;

C类地址192.0.0.0~223.255.255.255;

D类地址224.0.0.0~239.255.255.255；

E类地址240.0.0.0~255.255.255.255


私网IP范围是：

10.0.0.0～10.255.255.255

172.16.0.0～172.31.255.255

192.168.0.0～192.168.255.255


子网掩码为二进制下前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）
注意二进制下全是1或者全是0均为非法

注意：
1. 类似于【0.*.*.*】和【127.*.*.*】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，计数时可以忽略
2. 私有IP地址和A,B,C,D,E类地址是不冲突的

输入描述:
多行字符串。每行一个IP地址和掩码，用~隔开。

输出描述:
统计A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数，之间以空格隔开。

示例1
输入
10.70.44.68~255.254.255.0
1.0.0.1~255.0.0.0
192.168.0.2~255.255.255.0
19..0.~255.255.255.0
输出
1 0 1 0 0 2 1
'''

from functools import reduce

def ipv4toint(ip):
    try:
        ipNum = 0
        nodes = map(int, ip.split('.'))
        for node in nodes:
            nodeNum = int(node)
            if nodeNum < 0 or nodeNum > 255:
                return 0
            ipNum <<= 8
            ipNum += nodeNum
        return ipNum
    except Exception:
        return 0


def isIpv4Mask(mask):
    if mask == 0 or mask == ipv4toint('255.255.255.255'):
        return False
    else:
        prev = 0
        for _ in range(32):
            curr = mask & 1
            if curr < prev:
                return False
            prev = curr
            mask >>= 1
        return True

def ipv4toint_v1(ip):
    try:
        return reduce(lambda x, y: (x << 8) + y, map(int, ip.split('.')), 0)
    except Exception:
        return 0

def category(ipv4):
    ranges = {
        'a' : [ipv4toint('1.0.0.0'), ipv4toint('126.255.255.255')],
        'b' : [ipv4toint('128.0.0.0'), ipv4toint('191.255.255.255')],
        'c' : [ipv4toint('192.0.0.0'), ipv4toint('223.255.255.255')],
        'd' : [ipv4toint('224.0.0.0'), ipv4toint('239.255.255.255')],
        'e' : [ipv4toint('240.0.0.0'), ipv4toint('255.255.255.255')],
    }

    for k, v in ranges.items():
        if ipv4 >= v[0] and ipv4 <= v[1]:
            return k
    
    return ''

def isPrivate(ipv4):
    ranges = [
        [ipv4toint('10.0.0.0'), ipv4toint('10.255.255.255')],
        [ipv4toint('172.16.0.0'), ipv4toint('172.31.255.255')],
        [ipv4toint('192.168.0.0'), ipv4toint('192.168.255.255')],
    ]
    for v in ranges:
        if ipv4 >= v[0] and ipv4 <= v[1]:
            return True
    return False


def judge(line):
    ip, mask = line.split('~')
    ipNum = ipv4toint(ip)
    maskNum = ipv4toint(mask)
    if ipNum == 0 or maskNum == 0 or not isIpv4Mask(maskNum):
        return '', False, True
    
    return category(ipNum), isPrivate(ipNum), False
    
def solution():
    stats = {
        'a' : 0,
        'b' : 0,
        'c' : 0,
        'd' : 0,
        'e' : 0,
        'private' : 0,
        'error': 0,
    }
    line = ''
    while True:
        try:
            line = input()
        except Exception:
            break
        
        if line == '':
            break
        category, private, error = judge(line)
        if error:
            stats['error'] += 1
        else:
            if category != '':
                stats[category] += 1
            if private:
                stats['private'] += 1
    print("{a} {b} {c} {d} {e} {error} {private}".format(**stats))

if __name__ == '__main__':
    solution()