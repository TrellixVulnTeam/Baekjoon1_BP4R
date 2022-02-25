import sys
N = int(sys.stdin.readline().strip())
for _ in range(N):
    url = sys.stdin.readline().strip()
    print(f"URL #{N+1}")
    lst = ":".split(url)
    lst[0] = lst[0][2:]
    