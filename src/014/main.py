from functools import cache

@cache
def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


@cache
def collatz_sequence(n):
    length = 1
    while n != 1:
        n = collatz(n)
        length += 1
    return length

def main():
    max_length = 0
    max_number = 0
    for i in range(1, 1000000):
        length = collatz_sequence(i)
        if length > max_length:
            max_length = length
            max_number = i
    print(max_number)

if __name__ == '__main__':
    main()
