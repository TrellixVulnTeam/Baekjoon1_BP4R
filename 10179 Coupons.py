N = int(input())
for _ in range(0, N):
    inp = float(input())
    price = inp*0.8
    print('$' + "{:.2f}".format(price))