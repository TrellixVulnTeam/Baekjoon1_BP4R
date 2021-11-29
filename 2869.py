A,B,V = input().split()
days = int(V) / (int(A) - int(B))
if int(V)- (days - 1)* int(A) <= int(A):
    print(days + 1)
else:
    print(days)
