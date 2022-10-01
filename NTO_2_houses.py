data = input()
dataH = data.split()
n = int(dataH[0])
k = int(dataH[1])
pos = k


if k == 1:
    if (n % 2) == 0:
        while pos < (n-1):
            print(pos,end=' ')
            pos = pos + 2
        print(pos,end=' ')
        pos = n
        while pos > 2:
            print(pos,end=' ')
            pos = pos-2
        print(pos,end=' ')
    else:
        while pos < n:
            print(pos,end=' ')
            pos = pos + 2
        print(pos,end=' ')
        pos = n-1
        while pos > 2:
            print(pos,end=' ')
            pos = pos-2
        print(pos,end=' ')


        
if k == 2:
    if (n % 2) == 0:
        while pos < n:
            print(pos,end=' ')
            pos = pos + 2
        print(pos,end=' ')
        pos = n-1
        while pos > 1:
            print(pos,end=' ')
            pos = pos-2
        print(pos,end=' ')
    else:
        while pos < (n-1):
            print(pos,end=' ')
            pos = pos + 2
        print(pos,end=' ')
        pos = n
        while pos > 1:
            print(pos,end=' ')
            pos = pos-2
        print(pos,end=' ')     



if k == n-1:
    if (n % 2) == 0:
        while pos > 1:
            print(pos,end=' ')
            pos = pos - 2
        print(pos,end=' ')
        pos = 2
        while pos < n:
            print(pos,end=' ')
            pos = pos+2
        print(pos,end=' ')
    else:
        while pos > 2:
            print(pos,end=' ')
            pos = pos - 2
        print(pos,end=' ')
        pos = 1
        while pos < n:
            print(pos,end=' ')
            pos = pos+2
        print(pos,end=' ')     



if k == n:
    if (n % 2) == 0:
        while pos > 2:
            print(pos,end=' ')
            pos = pos - 2
        print(pos,end=' ')
        pos = 1
        while pos < (n-1):
            print(pos,end=' ')
            pos = pos+2
        print(pos,end=' ')
    else:
        while pos > 1:
            print(pos,end=' ')
            pos = pos - 2
        print(pos,end=' ')
        pos = 2
        while pos < (n-1):
            print(pos,end=' ')
            pos = pos+2
        print(pos,end=' ')     
