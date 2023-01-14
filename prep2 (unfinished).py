n = int(input())
f = int(input())
if f == 1:
    Ds = list(map(int,input().split()))
elif f == 2:
    s = list(map(int,input().split()))
    m = s[0]
    x = s[1]
    y = s[2]
    z = s[3]
    Ds = []
    Cs = list(map(int,input().split()))
    for i in range(n):
        if 1<=i and i<=m:
            Ds.append(Cs[i])
        elif m+1<=i and i<=n:
            Ds.append(((x*Ds[i-2]+y*Ds[i-1]+z)%10^9)+1)


"""for a in range(max(Ds)+1):
    t = 0
    p0 = 0 #n-1
    for p in range(n):
        try d = Ds[p0+p]
        except d = Ds[n-(p0+p)]"""
