"""
http://abc007.contest.atcoder.jp/tasks/abc007_2
"""


def test():
    b = input()

    if b == 'a':
        return -1

    if len(b) > 1:
        return b[:-1]

    return chr(ord(b[0]) - 1)

if __name__ == '__main__':
    print(test())
