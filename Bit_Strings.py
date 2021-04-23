M = 10**9 + 7
def fastp2(a):
    if a == 0:
        return 1
    if a == 1:
        return 2

    t = fastp2(a//2)
    t = t%M
    ans = (t*t)%M
    if a%2==1:
        ans*=2
        ans%=M
    return ans

n = int(input())
print(fastp2(n))
