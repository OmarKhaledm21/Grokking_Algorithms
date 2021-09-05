def NaiveGCD(a, b):
    gcd = 1
    for d in range(1, min(a, b) + 1):
        if (a % d == 0) and (b % d == 0):
            if d > gcd:
                gcd = d
    return gcd


""" EuclidGCD : a = bq + r -> gcd(b,r)"""
def EuclidGCD(a, b):
    if b == 0:
        return a
    r = a % b
    return EuclidGCD(b, r)




def main():
    print(EuclidGCD(1680, 640))
    print(sum([1,2,3]))


if __name__=="__main__":
    main()