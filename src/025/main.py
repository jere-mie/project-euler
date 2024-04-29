def main():
    a, b = 1, 0
    i = 2
    while True:
        temp = a
        a = a+b
        b = temp

        if len(str(a)) >= 1000:
            print(i)
            break
        i+=1

if __name__ == '__main__':
    main()
