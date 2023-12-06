def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def isFactor(i, num):
    return num%i == 0

def main():
    num = 600851475143
    factors = []
    for i in range(2, num):
        if i>num:
            break
        if isFactor(i, num):
            num/=i
            if isPrime(i):
                factors.append(i)
    print(max(factors))

if __name__ == '__main__':
    main()
