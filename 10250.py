n = int(input())
for num in range(0, n):
    room_number = 0
    H, W, N = input().split()
    H = int(H)
    W = int(W)
    N = int(N)
    if N% H != 0:
        room_number += N%H * 100
        room_number += (N // H + 1)
    else:
        room_number += H*100

        room_number += N//H
    print(room_number)


