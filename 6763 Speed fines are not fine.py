limit = int(input())
real = int(input())
over = real - limit
fine = 0
if over >= 1 and over <= 20:
    fine = 100
elif over >= 21 and over <= 30:
    fine = 270
elif over >= 31:
    fine = 500
else:
    fine = 0
if fine > 0:
    print(f"You are speeding and your fine is ${fine}.")
else:
    print("Congratulations, you are within the speed limit!")