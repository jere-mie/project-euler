def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def main():
    primes = [2]
    i = 3
    while True:
        if isPrime(i):
            primes.append(i)
        if len(primes) == 10001:
            break
        i+=1
    print(primes[-1])

if __name__ == '__main__':
    main()
