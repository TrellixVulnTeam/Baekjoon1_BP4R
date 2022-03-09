def towerOfHanoi(N, source, destination, auxiliary):
    if N == 1:
        print(source, destination)
        return
    towerOfHanoi(N - 1, source, auxiliary, destination)
    print(source, destination)
    towerOfHanoi(N - 1, auxiliary, destination, source)


N = int(input())
print(2**N-1)
towerOfHanoi(N, '1', '3', '2')

