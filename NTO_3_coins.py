n = int(input())
Ks = int(n*(n-1)/2)
Res = ''
a = False
b = False
dataFull = list()
for i in range (1, Ks+1):
    m = input()
    dataFull.append(m)

for j in range (1, len(dataFull)+1):
    data = dataFull[j-1]
    if data[1] == '>':
        for l in range (1, len(Res)+1):
            if data[0]==Res[l-1]:
                Ind0 = l-1
                Res1 = Res[0:l-1]
                Res2 = Res[l-1:len(Res)+1]
                a = True
        for l in range (1, len(Res)+1):
            if data[2]==Res[l-1]:
                Ind2 = l-1
                Res3 = Res[0:l]
                Res4 = Res[l:len(Res)+1]
                b = True
        if (a != b):
            if a == True:
                Res = Res1+data[2]+Res2
            if b == True:
                Res = Res3+data[0]+Res4
        elif (a == False) and (b == False):
                Res = Res+data[2]+data[0]
        elif (a== True) and (b == True):
            if Ind2 > Ind0:
                Ind = Res[Ind2]
                if Ind0<len(Res):
                    Res = Res[0:Ind2] + Res[Ind2+1:len(Res)]
                else:
                    Res = Res[0:Ind2]
                Res5 = Res[0:Ind0]
                Res6 = Res[Ind0:len(Res)+1]
                Res = Res5+Ind+Res6    
        
        a = False
        b = False
    elif data[1] == '<':
        for l in range (1, len(Res)+1):
            if data[2]==Res[l-1]:
                Ind2 = l-1
                Res1 = Res[0:l-1]
                Res2 = Res[l-1:len(Res)+1]
                a = True
        for l in range (1, len(Res)+1):
            if data[0]==Res[l-1]:
                Ind0 = l-1
                Res3 = Res[0:l]
                Res4 = Res[l:len(Res)+1]
                b = True
        if (a != b):
            if a == True:
                Res = Res1+data[0]+Res2
            if b == True:
                Res = Res3+data[2]+Res4
        elif (a == False) and (b == False):
            Res = Res+data[0]+data[2]
        elif (a== True) and (b == True):
            if Ind0 > Ind2:
                Ind = Res[Ind0]
                if Ind0<len(Res):
                    Res = Res[0:Ind0] + Res[Ind0+1:len(Res)]
                else:
                    Res = Res[0:Ind0]
                Res5 = Res[0:Ind2]
                Res6 = Res[Ind2:len(Res)+1]
                Res = Res5+Ind+Res6            
        a = False
        b = False
print(Res)
        
