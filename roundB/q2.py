T = int(input())
for x in range(1, T + 1):
    N,D = map(int, input().split())
    buses = list(map(int,input().split()))
    i = N -1
    while D > 0 and i >= 0:
        rest = D % buses[i]
        if rest != 0:
            D -= rest
        i -= 1

    print("Case #{}: {}".format(x, D), flush = True)