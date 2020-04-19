from copy import deepcopy
T = int(input())
for x in range(1, T + 1):
    N,D = map(int, input().split())
    buses = list(map(int,input().split()))
    first = buses[0]
    i = D // first
    y = 0
    while i > 0:
        alt = deepcopy(buses)
        start = i * first
        for j in range(start, D+1):
            while alt:
                #print(j, alt[bus], alt)
                if j % alt[0] == 0:
                    #print(alt[bus],j)
                    alt.pop(0)
                else:
                    break
        if not alt:
            y = start
            break
        i -= 1

    print("Case #{}: {}".format(x, y), flush = True)