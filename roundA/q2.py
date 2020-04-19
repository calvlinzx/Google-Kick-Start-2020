def ch(P, sums, row1, row2, anss):
    for i in range(P - 1):
            ans = sums[row1][i] + sums[row2][P - i - 2]
            anss.append(ans)
    if len(sums[row1]) >= P:
        anss.append(sums[row1][P-1])
        anss.append(sums[row2][P-1])

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
        ch(P, sums, 0, 1, anss)
        y = max(anss)
    elif N == 3:

        i = j = 0
        while i <= P and i <= N:
            while j <= P-i and j <= N:
                ans = 0
                if i:
                    ans += sums[0][i - 1]
                if j:
                    ans += sums[1][j - 1]
                if P-i-j > 0 and P - i - j <= N:
                    ans += sums[2][P-i-j-1]
                j += 1
                # if i == 0:
                #     ans = sums[1][j-1] + sums[2][P - i - j-1]
                # elif j == 0:
                #     ans = sums[0][i-1] + sums[2][P-i-j-1]
                # elif P-i-j == 0:
                #     ans = sums[0][i-1] + sums[1][j-1]
                # else:
                #     ans = sums[0][i-1] + sums[1][j-1] + sums[2][P - i - j-1]
                anss.append(ans)
            i += 1
        y = max(anss)
    print("Case #{}: {}".format(x, y), flush = True)