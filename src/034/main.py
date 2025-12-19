from functools import cache

@cache
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)

def main():
    total = 0
    for i in range(10, 100000):
        if i == sum(factorial(int(digit)) for digit in str(i)):
            total += i
    print(total)

if __name__ == '__main__':
    main()
