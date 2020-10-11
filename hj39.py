#encoding: utf-8


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


def solution():
    mask = ipv4toint(input())
    ip1= ipv4toint(input())
    ip2 = ipv4toint(input())
    if mask == 0 or ip1 == 0 or ip2 == 0 or not isIpv4Mask(mask):
        print(1)
    elif mask & ip1 == mask & ip2:
        print(0)
    else:
        print(2)

    
    

if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            print(e)
            break