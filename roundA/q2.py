def ch(P, sums, anss):
    for i in range(P - 1):
            print(sums[0], sums[1])
            ans = sums[0][i] + sums[1][P - i - 2]
            anss.append(ans)
    y = max(anss)
    return y

T = int(input())
for x in range(1, T + 1):
    N,K,P = map(int, input().split())
    stacks = {}
    for i in range(N):
        stacks[i] = list(map(int, input().split()))
    sums = {}
    for i, l in stacks.items():
        l2 = []
        for j in range(len(l)):
            l2.append(sum(l[:j+1]))
        sums[i] = l2

    anss = []

    if N ==1:
        y = sums[0][P - 1]
    elif N == 2:
        for i in range(P - 1):
            print(sums[0], sums[1])
            ans = sums[0][i] + sums[1][P - i - 2]
            anss.append(ans)
        y = max(anss)
    elif N == 3:
        for i in range(P-1):
            for j in range(P-i-1):
                ans = sums[0][i] + sums[1][j] + sums[2][P - i - j - 3]
                anss.append(ans)
        y = max(anss)
    print("Case #{}: {}".format(x, y), flush = True)