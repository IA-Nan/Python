
def gcd(x, y):
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)

if __name__ == "__main__":
        a = int(input("a = "))
        b = int(input("b = "))
        c = gcd(a, b)
        print(c)
        c = lcm(a, b)
        print(c)



""" def is_prime(num):
    判断一个数是不是
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True if num != 1 else False

def main():
    a = int(input("输入一个数"))
    b = is_prime(a)
    print(b)


if __name__ == "__main__":

    main() """



