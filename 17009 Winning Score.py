apples = 0
bananas = 0

apples += int(input()) * 3

apples += int(input()) * 2

apples += int(input())

bananas += int(input()) * 3

bananas += int(input()) * 2

bananas += int(input())


if apples == bananas:
    print("T")
if apples > bananas:
    print("A")
if apples < bananas:
    print("B")