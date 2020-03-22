T = int(input())
for x in range(1, T + 1):
    N,K = map(int, input().split())
    ts = list(map(int,input().split()))
    diffs = []
    for i,t in enumerate(ts):
        if i + 1 <= (len(ts) - 1):
            diff = ts[i+1] - t
            diffs.append(diff)
    max_diff = max(diffs)
    diffs.remove(max_diff)
    if max_diff % 2 == 0:
        diffs.append(max_diff // 2)
    else:
        diffs.append(max_diff // 2 + 1)
    y = max(diffs)

    print("Case #{}: {}".format(x, y), flush = True)