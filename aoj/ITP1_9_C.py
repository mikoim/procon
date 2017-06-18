n = int(input())

a = 0
b = 0

for _ in range(n):
    word_a, word_b = input().split()

    words = [word_a, word_b]
    words.sort()

    if word_a == word_b:
        a += 1
        b += 1
    elif words.index(word_a) == 1:
        a += 3
    else:
        b += 3

print(a, b)
