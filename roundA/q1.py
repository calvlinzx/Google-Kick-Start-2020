T = int(input())
for x in range(1, T + 1):
    N,B = map(int, input().split())
    prices = list(map(int,input().split()))
    prices.sort(reverse = False)
    y = 0
    spent = 0
    for i in range(N):
        if spent + prices[i] <= B:
            spent += prices[i]    
            y += 1

    print("Case #{}: {}".format(x, y), flush = True)