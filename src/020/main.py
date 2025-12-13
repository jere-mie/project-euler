from math import factorial

def main():
    print(sum(int(digit) for digit in str(factorial(100))))

if __name__ == '__main__':
    main()
