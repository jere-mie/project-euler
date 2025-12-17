def main():
    results = set()
    for a in range(2, 101):
        for b in range(2, 101):
            results.add(a ** b)
    print(len(results))

if __name__ == '__main__':
    main()
