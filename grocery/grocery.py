items = {}

while True:
    try:
        item = input().strip().upper()
        items[item] = items.get(item, 0) + 1
    except EOFError:
        break

for item in sorted(items):
    print(items[item], item)
