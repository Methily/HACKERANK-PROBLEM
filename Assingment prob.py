comb_dict = {}


def nchoosek(n, k_in):
    k = min(k_in, n - k_in)
    if n < k or k < 0:
        return 0
    elif (n, k) in comb_dict:
        return comb_dict[(n, k)]
    elif k == 0:
        return 1
    elif n == k:
        return 1
    else:
        a = 1
        for cnt in range(k):
            a *= (n - cnt)
            a //= (cnt + 1)
            comb_dict[(n, cnt + 1)] = a
        return a


T = int(input())
for cntT in range(T):
    M, N = [int(_) for _ in input().split()]
    arr = []
    for k in range(2, M + 2):
        a = 1
        s = 0
        for i in range(M // k + 2):
            if (M < i * k):
                break
            s += a * nchoosek(N, i) * nchoosek(N - 1 + M - i * k, M - i * k)
           
            a *= -1
        arr.append(s)
       
    total = arr[-1]
    # print(new_total)
    diff = [arr[0]] + [arr[cnt + 1] - arr[cnt] for cnt in range(M - 1)]
   
    output = sum(diff[cnt] * (cnt + 1) / total for cnt in range(M))
    print(output)
