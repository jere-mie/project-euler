def d(n):
    return sum(i for i in range(1, n) if n % i == 0)

def main():
    tot = 0
    for i in range(1, 10000):
        j = d(i)
        if i == d(j) and i != j:
            tot += i
    print(tot)

if __name__ == '__main__':
    main()
