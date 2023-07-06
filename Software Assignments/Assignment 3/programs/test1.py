def fromBinary(nbin,dbin,n):
    bins = bin(nbin)[2:]
    dbins = bin(dbin)[2:]
    ch = 97+n-1
    lst=[]
    for i in range (0,len(bins)):
        if(i<len(dbins)):
            if(dbins[len(dbins)-i-1] == '1'): 
                ch-=1
                continue
            elif(bins[len(bins)-i-1] == '1'): lst.append(chr(ch))
            elif(bins[len(bins)-i-1] == '0'): lst.append(chr(ch)+"'")
        else:
            if(bins[len(bins)-1-i] == '1'): lst.append((chr(ch)))
            elif(bins[len(bins)-1-i] == '0'): lst.append((chr(ch))+"'")
        ch-=1
    for i in range(len(bins),n):
        lst.append(chr(ch)+"'")
        ch-=1
    lst.reverse()
    str = ''.join(lst)
    return str

print(fromBinary(1,0,4))