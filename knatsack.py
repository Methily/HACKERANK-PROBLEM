def unboundedKnapsack(k, arr):
    dp = [0] * (k + 1)
    for i in range(1, k + 1):
        for j in arr:
            if j <= i:
                dp[i] = max(dp[i], dp[i - j] + j)
    return dp[k]

if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for _ in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        arr = list(map(int, input().rstrip().split()))
        result = unboundedKnapsack(k, arr)
        fptr.write(str(result) + '\n')
    fptr.close()