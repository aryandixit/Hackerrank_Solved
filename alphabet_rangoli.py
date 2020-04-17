n = int(input())
alpha = {}
bet = 97
for i in range(1,27):
    alpha[i] = chr(bet)
    bet = bet + 1
for i in range(n,0,-1):
        for k in range(i,1,-1):
            print(end="--")
        for j in range(n,i-1,-1):
            print((alpha[j]),end ='')
            if i != n:
                for q in range(1):
                    print(end ="-")
        for l in range(i+1,n+1):
            print((alpha[l]),end ='')
            if l != n:
                for r in range(1):
                    print(end = "-")
        for m in range(i,1,-1):
            print(end="--")
        print("")
for i in range(1,n):   
        for l in range(1,i+1):
            print(end="--")
        for j in range(n,i,-1):
            print(alpha[j],end="")
            if i != n-1:
                for q in range(1):
                    print(end="-")
        for k in range(i+2,n+1):
            print(alpha[k],end="")
            if k != n:
                for r in range(1):
                    print(end="-")
        for m in range(1,i+1):
            print(end="--")
        print("")
