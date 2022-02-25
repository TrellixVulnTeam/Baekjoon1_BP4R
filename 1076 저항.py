first = input()
second = input()
third = input()
val = {}
m = {}
val["black"] = 0
val["brown"] = 1
val["red"] = 2
val["orange"] = 3
val["yellow"] = 4
val["green"] = 5
val["blue"] = 6
val["violet"] = 7
val["grey"] = 8
val["white"] = 9

m["black"] = 1
m['brown'] = 10
m['red'] = 100
m['orange'] = 1000
m['yellow'] = 10000
m['green'] = 100000
m['blue'] = 1000000
m['violet'] = 10000000
m['grey'] = 100000000
m['white'] = 1000000000

answer = ''
answer += str(val[first])
answer += str(val[second])
answer = int(answer) * m[third]
print(answer)