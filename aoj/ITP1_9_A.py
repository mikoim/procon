from collections import Counter

word = input()
count = 0

while True:
    text = input()
    if text == 'END_OF_TEXT':
        break

    count += Counter(text.lower().split())[word.lower()]

print(count)
