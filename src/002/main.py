def main():
    a, b = 1, 2
    tot = 2
    while True:
        a, b = b, a+b
        if b%2 == 0:
            tot+=b
        if b > 4000000:
            print(tot)
            break

if __name__ == '__main__':
    main()    