t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    
    gotIt = 0

    for i, icecreamI in enumerate(a):
        for j, icecreamJ in enumerate(a):
            if i != j:
                if icecreamI + icecreamJ == m:
                    print(str(i+1)+ ' ' + str(j+1))
                    gotIt +=1
                    break
        if gotIt > 0:
            break