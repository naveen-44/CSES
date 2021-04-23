def tz(n):
    ans = 0
    x = 5
    while(x<=n):
        ans += n//x
        x*=5
    return ans
n = int(input())
print(tz(n))
