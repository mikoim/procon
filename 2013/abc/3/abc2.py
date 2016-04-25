"""
http://abc003.contest.atcoder.jp/tasks/abc003_2
"""


# ToDo: Fix broken? script


def main():
    at = 'a t c o d e r'.split()
    a, b = [list(input()) for _ in range(2)]
    for i in range(len(a)):
        print(a[i], b[i])
        if (a[i] is b[i]) or (a[i] is '@' and b[i] in at) or (b[i] is '@' and a[i] in at):
            continue
        print('You will lose')
        return
    print('You can win')


if __name__ == '__main__':
    main()
