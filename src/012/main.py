def number_of_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 2  # i and n/i
    if int(n**0.5)**2 == n:
        count -= 1 # perfect squares
    return count

def main():
    triangle = 0
    for i in range(1, 100000):
        triangle+= i
        if number_of_divisors(triangle) > 500:
            print(triangle)
            break

if __name__ == '__main__':
    main()
