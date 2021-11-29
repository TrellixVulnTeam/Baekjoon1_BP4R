import math
def gcd(a, b):
    if a == b or a == 0 or b == 0:
        return max(a, b)
    return gcd(min(a, b), max(a, b)%min(a, b))

if __name__ == '__main__':
    x, y = map(int, input().split())
    cx, cy, dx, dy = map(int, input().split())
    min_distance = math.sqrt((x - cx)**2 + (y - cy)**2)
    dx, dy = dx // gcd(dx, dy), dy // gcd(dx, dy)
    while True:
        cx += dx
        cy += dy
        if math.sqrt((x - cx)**2 + (y - cy)**2) < min_distance:
            min_distance = math.sqrt((x - cx)**2 + (y - cy)**2)
        else:
            cx -= dx
            cy -= dy
            break
    print(cx, cy)
