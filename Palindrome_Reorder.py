s = raw_input()
pl = [0 for i in range(27)]

for i in range(len(s)):
    pl[ord(s[i])-65]+=1

flag = 0
p = -1
for i in range(len(pl)):
    if pl[i]%2!=0:
        flag+=1
        p=i
    if flag>1:
        print("NO SOLUTION")
        break
ans = ''
for i in range(26):
    if i != p:
        ans = ans + chr(i+65)*(pl[i]//2)
        
if flag==1:
    ans+=chr(p+65)*pl[p]

for i in range(25,-1,-1):
    if i != p:
        ans = ans + chr(i+65)*(pl[i]//2)
if flag<=1:
    print(ans)
