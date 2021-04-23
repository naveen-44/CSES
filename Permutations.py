n = int(input())
if(n>1 and n<4):
    print("NO SOLUTION")
else:
    l = []
    for i in range(2,n+1,2):
        l.append(i)
    for i in range(1,n+1,2):
        l.append(i)
    for ll in l:
        print(ll,end = " ")
