n = int(input())
cards = {
    'S': [],
    'H': [],
    'C': [],
    'D': []
}

for _ in range(n):
    color, rank = input().split()
    cards[color].append(rank)

for color in ['S', 'H', 'C', 'D']:
    for rank in [x for x in range(1, 14) if str(x) not in cards[color]]:
        print(color, rank)
