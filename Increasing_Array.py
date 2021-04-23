n = int(input())
l = list(map(int,input().split()))
ans = 0
for i in range(1,len(l)):
    if(l[i]<l[i-1]):
        x = (l[i-1]-l[i])
        ans+=x
        l[i] = l[i]+x
print(ans)
