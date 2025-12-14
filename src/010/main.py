def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    primes = [2]
    for i in range(3, 2_000_000, 2):
        if is_prime(i):
            primes.append(i)
    print(sum(primes))

if __name__ == '__main__':
    main()
