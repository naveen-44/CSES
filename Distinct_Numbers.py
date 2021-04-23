n = int(input())
l = list(map(int,input().split()))
a = sorted(l)
ans = 1
p = a[0]
for i in range(1,len(a)):
    x = a[i]
    if(x!=p):
        ans+=1
    p = x
print(ans)
