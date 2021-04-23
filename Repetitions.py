s = input()
c = 0
p = ''
ans = 0
for i in range(len(s)):
    x = s[i]
    if(x!=p):
        ans = max(c,ans)
        c=1
    else:
        c+=1
    p = x
print(max(ans,c))
