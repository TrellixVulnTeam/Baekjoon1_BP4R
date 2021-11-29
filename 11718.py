while True:
    try:
        print(input())
    except EOFError:
        quit()