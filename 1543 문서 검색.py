word = input()
key = input()
count = 0
i = 0

while i < len(word) - len(key):
    if word[i:i + len(key)] == key:
        count += 1
        i += len(key)
    else:
        i += 1
print(count)
    