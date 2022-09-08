from xml.etree.ElementTree import tostring

def cmp(a,b):
    return (len(a[2]) < len(b[2]))

def toBinary(str):
    bin,dbin,cd,cb = 0,0,0,0
    for i in range(0, len(str)):
        if(str[i].isalpha()):
            if(i+1>=len(str)): cb=1
            elif(str[i+1] == '\''): cb=0
            else: cb=1
            bin = bin*2+cb
        elif(str[i] == '-'):
            cd=1
            dbin = dbin*2+cd
    return [bin,dbin]

def fromBinary(nbin,dbin,n):
    bins = bin(nbin)
    bins=bins[2:]
    dbins = bin(dbin)
    dbins=dbins[2:]
    ch = 97+n
    lst=[]
    ch -= n-len(bins)
    for i in range (0,len(bins)):
        if(i<len(dbins)):
            if(dbins[len(dbins)-i-1] == '1'): 
                ch-=1
                continue
            elif(bins[len(bins)-i-1] == '1'): lst.append(chr(ch))
            elif(bins[len(bins)-i-1] == '0'): lst.append(chr(ch)+"'")
        else:
            if(bins[len(bins)-1-i] == '1'): lst.append(tostring(chr(ch)))
            elif(bins[len(bins)-1-i] == '0'): lst.append(tostring(chr(ch))+"'")
        ch-=1
    lst.reverse()
    str = ''.join(lst)
    print(str)

def combine(group,ans):
    groups = [ [] for _ in range(len(group)) ]
    set1,set2 = set(),set()
    for i in range(0, len(group)-1):
        for j in range(0, len(group[i])):
            check = False
            for k in range(0, len(group[i+1])):
                if(group[i][j][1] == group[i+1][k][1]):
                    tset = set()
                    xor = group[i][j][0] ^ group[i+1][k][0]
                    if((xor&(xor-1)) == 0):
                        b = xor.bit_length()
                        # y = ((group[i][j][0]>>b)<<(b-1)) + (group[i][j][0] & ((1<<(b-1))-1))
                        y = max(group[i][j][0],group[i+1][k][0])
                        tset = tset.union(group[i][j][2])
                        tset = tset.union(group[i+1][k][2])
                        set2.add((group[i+1][k][0],group[i+1][k][1]))
                        check = True
                        groups[bin(y).count("1")].append((y,xor+group[i][j][1],tset))
            if(check == False): 
                if(((group[i][j][0],group[i][j][1]) in set1) == False):
                    ans.append(group[i][j])
        set1 = set2
        set2 = set()
        print(groups)
    x = len(group) - 1
    for i in range(len(group[len(group)-1])):
        if(((group[x][i][0],group[x][i][1]) in set1) == False):
            ans.append(group[x][i])
    final = True
    for i in groups:
        if(len(i) != 0):
            final = False
    if(final):
        return ans
    else:
        return combine(groups,ans)

def comb_function_expansion(func_TRUE, func_DC):
    """
    determines the maximum legal region for each term in the K-map function
    Arguments:
    func_TRUE: list containing the terms for which the output is '1'
    func_DC: list containing the terms for which the output is 'x'
    Return:
    a list of terms: expanded terms in form of boolean literals
    """
    n=0
    dict = {}
    for ch in func_TRUE[0]:
        if(ch.isalpha()): n+=1
    groups = [ [] for _ in range(n+1) ]
    truebin, dcbin = [],[]
    it = 0
    for each in func_TRUE:
        binary = toBinary(each)
        truebin.append(binary)
        groups[bin(binary[0]).count("1")].append((binary[0],binary[1],{binary[0]}))
        dict[binary] = it
        it += 1
    for each in func_DC:
        binary = toBinary(each)
        dcbin.append(binary)
        groups[bin(binary[0]).count("1")].append((binary[0],binary[1],{binary[0]}))
    print(groups)
    ans = combine(groups,[])
    ans.sort(cmp)
    output = [ None for _ in range(it)]
    completeset = set()
    for i in ans:
        completeset = completeset - i[2]


fromBinary(5,4,4)
# comb_function_expansion(["a'bc'd'", "abc'd'", "a'b'c'd", "a'bc'd", "a'b'cd"],["abc'd"])
# ["a'b'c'd'","a'b'c'd","a'b'cd'","a'bc'd'","ab'c'd'","a'bcd'","ab'c'd","ab'cd","abc'd","abcd","abcd"],[]