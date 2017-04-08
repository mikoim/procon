"""
B. Tidy Numbers
"""


def main():
    t = int(input())
    for i in range(1, t + 1):
        target = int(input())
        while not is_tidy(target):
            target = last_tidy(target)
            break
        print("Case #{}: {}".format(i, target))


def last_tidy(n):
    """
    >>> last_tidy(132)
    129
    >>> last_tidy(1000)
    999
    >>> last_tidy(7)
    7
    >>> last_tidy(111111111111111110)
    99999999999999999
    """

    if len(str(n)) == 1 or is_continuous(n) or is_tidy(n):
        return n
    elif is_lower(n):
        return int(str(n)[0] + '0' * len(str(n)[1:])) - 1
    else:
        a = [int(x) for x in str(n)]
        h_i = 0

        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                h_i = i - 1
                break

        return int(''.join(map(str, a[:h_i])) + str(a[h_i] - 1) + '9' * (len(a) - h_i - 1))


def is_tidy(n):
    """
    >>> is_tidy(8)
    True
    >>> is_tidy(123)
    True
    >>> is_tidy(555)
    True
    >>> is_tidy(224488)
    True
    >>> is_tidy(20)
    False
    >>> is_tidy(321)
    False
    >>> is_tidy(495)
    False
    >>> is_tidy(999990)
    False
    """

    a = [int(x) for x in str(n)]

    for i in range(1, len(a)):
        if not (a[i - 1] <= a[i]):
            return False

    return True


def is_continuous(n):
    """
    >>> is_continuous(11)
    True
    >>> is_continuous(12)
    False
    """

    return len(set(str(n))) == 1


def is_lower(n):
    """
    >>> is_lower(554)
    True
    >>> is_lower(556)
    False
    """

    a = str(n)
    return n < int(a[0] * len(a))


if __name__ == '__main__':
    main()
