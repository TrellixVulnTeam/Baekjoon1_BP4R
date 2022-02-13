weekly = int(input())
daily = int(input())
answer = "White"
if weekly <= 50 and daily <= 10:
    answer = "White"
elif daily > 30:
    answer = "Red"
else:
    answer = "Yellow"

print(answer)
