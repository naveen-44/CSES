t = int(input())
for tt in range(t): 
    ans = 0
    i,j = input().split()
    i,j = int(i),int(j)
    n = max(i,j)
    m = min(i,j)
    z = n*n
    if i==j:
        ans = i*i - (i-1)
    elif(i>j):
        if n%2==0:
            ans = z - m + 1
        else:
            ans = z - 2*n + m + 1
    else:
        if n%2==1:
            ans = z - m + 1
        else:
            ans = z - 2*n + m + 1
    print(ans)
