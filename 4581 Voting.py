while True:
    votes = input()
    if votes == '#':
        quit()
    full = len(votes)
    yes = 0
    no = 0
    need = 0
    for v in votes:
        if v == "Y":
            yes += 1
        if v == "N":
            no += 1
        if v == "A":
            need += 1
    if need >= full / 2:
        print("need quorum")
        continue
    else:
        if yes > no:
            print("yes")
        elif yes == no:
            print("tie")
        else:
            print("no")
    
    