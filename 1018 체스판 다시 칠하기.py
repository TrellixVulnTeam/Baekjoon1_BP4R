N, M = map(int, input().split())
board = []
minimum = 64
for n in range(0, N):
    board.append(input())
for y in range(0, N):
    if N - y >= 8:
        for x in range(0, M):
            Wcount = 0
            Bcount = 0
            count = 0
            if M - x >= 8:
                for ar in range(y, y + 8):
                    for square in range(x, x + 8):
                
                        if count % 2 == 0:
                            if board[ar][square] == "W":
                                Bcount += 1
                            if board[ar][square] == "B":
                                Wcount += 1
                        else:
                            if board[ar][square] == "B":
                                Bcount += 1
                            if board[ar][square] == "W":
                                Wcount += 1
                
                        count += 1
                    count += 1
                minimum = min(minimum, Bcount, Wcount)
print(minimum)

"""minimum이 0인 경우 따로 생각해서 바꾸는 것이 안됨:
하나도 안 바꿔도 되는 판에서 옮겼더니 바꿔야 되면 제대로 카운팅되지 않음"""
