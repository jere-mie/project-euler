def isPalindrome(n):
    return str(n) == str(n)[::-1]

def main():
    pal = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            if isPalindrome(i*j) and i*j > pal:
                pal = i*j
    print(pal)

if __name__ == '__main__':
    main()
