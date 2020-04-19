T = int(input())
for x in range(1, T + 1):
    n = int(input())
    hs = list(map(int,input().split()))
    count = 0
    for i in range(1, n-1):
        if hs[i-1] < hs[i] and hs[i] > hs[i+1]:
            count += 1

    print("Case #{}: {}".format(x, count), flush = True)