"""
http://abc005.contest.atcoder.jp/tasks/abc005_3
"""


def test():
    t = int(input())  # 何秒以内のたこ焼きまで売るか

    n = int(input())  # 高橋君が作成するたこ焼きの総数
    a = list(map(int, input().split()))  # それぞれのたこ焼きが何秒後にできるか

    m = int(input())  # 来店するお客さんの人数
    b = list(map(int, input().split()))  # それぞれのお客さんが何秒後に来るか

    if n < m:
        return 'no'

    stock = []

    end = max(max(a), max(b)) + t
    time = 1

    while time < end:
        if len(b) == 0:
            break

        if len(a) > 0 and a[0] == time:
            del a[0]
            stock.append(t + 1)
            continue

        if b[0] == time:
            del b[0]
            if len(stock) == 0:
                return 'no'
            else:
                stock.pop(0)
            continue

        stock = list(filter(lambda x: x > 0, map(lambda x: x - 1, stock)))

        time += 1

    return 'yes'


if __name__ == '__main__':
    print(test())
