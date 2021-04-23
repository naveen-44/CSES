def sumn(n):
    return n*(n+1)//2

n = int(input())
s = sumn(n)
if s%2==1:
    print("NO")
else:
    print("YES")
    l1 = []
    l2 = []
    target = s//2
    for i in range(n,0,-1):
        if target-i>=0:
            l1.append(i)
            target-=i
        else:
            l2.append(i)
    print(len(l1))
    ans1 = ''
    for k in l1:
        ans1+=str(k) + str(" ")
    print(ans1)
    ans2 = ''
    print(len(l2))
    for k in l2:
        ans2 += str(k) + str(" ")
    print(ans2)
