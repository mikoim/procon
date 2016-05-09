def main():
    t = int(input())

    for i in range(t):
        n, k = map(int, input().split())
        s = list(map(int, input().split()))
        l = sum(y > 0 for y in s)

        if n - l < k:
            print('YES')
        else:
            print('NO')

if __name__ == "__main__":
    main()