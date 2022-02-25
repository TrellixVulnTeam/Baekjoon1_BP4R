while True:
    n = int(input())
    answer = []
    if n == -1:
        quit()
    for num in range(1, n):
        if n % num == 0:
            answer.append(num)
    if sum(answer) == n:
        bot = " + ".join(list(map(str, answer)))
        print(f"{str(n)} = {bot}")
    else:
        print(f"{n} is NOT perfect.")