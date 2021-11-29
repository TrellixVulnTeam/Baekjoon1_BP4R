word = input()
count = len(word)
for n in range(1, len(word)):
    if word[n-1: n+1] == 'c=' or word[n-1:n+ 1] == 'c-' or word[n-1:n+ 1] == 'd-' or word[n-1:n+ 1] == 'lj' or word[n-1:n+ 1] == 'nj' or word[n-1:n+ 1] == 's=' or word[n-1:n+ 1] == 'z=':
        count -= 1
    else:
        continue
for num in range(2, len(word)):
    if word[num - 2: num + 1] == 'dz=':
        count -= 1

print(count)

