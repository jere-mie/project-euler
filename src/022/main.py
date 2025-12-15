def main():
    print(sum((i + 1) * sum(ord(c) - ord('A') + 1 for c in name) for i, name in enumerate(sorted([i.replace('"', '') for i in open('names.txt', 'r').read().split(',')]))))
    
if __name__ == '__main__':
    main()
