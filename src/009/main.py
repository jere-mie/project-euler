def main():
    for a in range(1, 1000):
        for b in range(a, 1000):
            c = (a**2 + b**2)**0.5
            if abs(c-int(c)) > 0.001:
                continue
            c = round(c)
            if  a+b+c == 1000 and a!=c and b!=c:
                print(a, b, c)
                print(a*b*c)
                return

if __name__ == '__main__':
    main()
