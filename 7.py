n, k, m = map(int, input().split())
if k < m:
    print(m - k - 1)
else:
    print(n - k + m - 1)
