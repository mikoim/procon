while True:
    text = input()

    if text == '-':
        break

    m = int(input())

    for _ in range(m):
        h = int(input())
        text = text[h:] + text[:h]

    print(text)
