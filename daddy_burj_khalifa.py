n = int(input())
l = len(bin(n)[2:])
for i in range(1,n+1):
    print("{} {} {} {}".format(str(i).rjust(l),oct(i)[2:].rjust(l),hex(i)[2:].upper().rjust(l),bin(i)[2:].rjust(l)),sep = '')
    
