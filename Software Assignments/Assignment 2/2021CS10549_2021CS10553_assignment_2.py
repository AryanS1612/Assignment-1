from pickle import NONE

def custom_print(groups,n):
    it = 0
    Empty = (None,'{}')
    if(len(groups)==0):
        print("Terms of the answer after this iteration are :")
        print(Empty)
    elif((type(groups[0]) == tuple)):
        print("Terms of the answer after this iteration are :")
        for i in groups:
            decoded = fromBinary(i[0],i[1],n)
            terms = set()
            for k in i[2]:
                terms.add(fromBinary(k,0,n))
            final = (decoded,terms)
            print("     ",final)
    else:
        for i in groups:
            print("Group number",it)
            if(len(i) == 0):
                print("     ",Empty)
            else:
                for j in i:
                    decoded = fromBinary(j[0],j[1],n)
                    terms = set()
                    for k in j[2]:
                        terms.add(fromBinary(k,0,n))
                    final = (decoded,terms)
                    print("     ",final)
            it += 1

def toBinary(str):
    bin,cb = 0,0
    for i in range(0, len(str)):
        if(str[i].isalpha()):
            if(i+1>=len(str)): cb=1
            elif(str[i+1] == '\''): cb=0
            else: cb=1
            bin = bin*2+cb
    return bin

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

def combine(group,ans,n):
    groups = [ [] for _ in range(len(group)-1) ]
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
                        y = group[i+1][k][0]
                        tset = tset.union(group[i][j][2])
                        tset = tset.union(group[i+1][k][2])
                        set2.add((group[i+1][k][0],group[i+1][k][1]))
                        check = True
                        index = bin(y).count("1")-bin(xor+group[i][j][1]).count("1") 
                        groups[index].append((y,xor+group[i][j][1],tset))
            if(check == False): 
                if(((group[i][j][0],group[i][j][1]) in set1) == False): ans.append(group[i][j])
        set1 = set2
        set2 = set()
    x = len(group) - 1
    for i in range(len(group[len(group)-1])):
        if(((group[x][i][0],group[x][i][1]) in set1) == False): ans.append(group[x][i])
    final = True
    for i in groups:
        if(len(i) != 0): final = False
    # custom_print(ans,n)
    # print()
    # print('New iteration')
    # print("printing groups")
    # custom_print(groups,n)
    if(final): return ans
    else: return combine(groups,ans,n)

def comb_function_expansion(func_TRUE, func_DC):
    """
    determines the maximum legal region for each term in the K-map function
    Arguments:
    func_TRUE: list containing the terms for which the output is '1'
    func_DC: list containing the terms for which the output is 'x'
    Return:
    a list of terms: expanded terms in form of boolean literals
    """
    n = 0
    dict = {}
    for ch in func_TRUE[0]:
        if(ch.isalpha()): n+=1
    groups = [ [] for _ in range(n+1) ]
    truebin, dcbin = [],[]
    it = 0
    for each in func_TRUE:
        binary = toBinary(each)
        truebin.append(binary)
        groups[bin(binary).count("1")].append((binary,0,{binary}))
        dict[binary] = it
        it += 1
    for each in func_DC:
        binary = toBinary(each)
        dcbin.append(binary)
        groups[bin(binary).count("1")].append((binary,0,{binary}))
    # print("printing groups")
    # custom_print(groups,n)
    ans = combine(groups,[],n)
    ans.sort(key = lambda x: -len(x[2]))
    output = [ None for _ in range(it)]
    completeset = set(dcbin)
    for each in ans:
        nonset = each[2] - completeset
        s = fromBinary(each[0],each[1],n)
        for element in nonset:
            if(s == ''):
                output[dict[element]] = None
            else:
                output[dict[element]] = s
        completeset = completeset.union(nonset)
    return output

# print(comb_function_expansion(["a'bc'd'", "abc'd'", "a'b'c'd", "a'bc'd", "a'b'cd"],["abc'd"]))
# print(comb_function_expansion(["a'b'c'd", "a'b'cd", "a'bc'd", "abc'd'", "abc'd", "ab'c'd'", "ab'cd"],["a'bc'd'", "a'bcd", "ab'c'd"]))
# print(comb_function_expansion(["a'b'c", "a'bc", "a'bc'", "ab'c'"],["a'c", "a'b", "ac'"]))
# print(comb_function_expansion(["abc'","a'bc","abc"],["a'b'c","ab'c"]))
# print(comb_function_expansion(["a'b'c'", "ab'c'", "a'bc", "a'bc'", "abc'"],["ab'c"]))
# print(comb_function_expansion(["a'b'cdefgh", "a'b'cdefgh'", "a'b'cdef'gh'", "a'b'cd'e'fgh", "a'bcd'ef'gh'", "a'bcdefgh'", "a'bc'd'e'fg'h", "abc'd'e'fg'h", "a'bc'd'efgh'", "abc'd'efgh'", "abc'def'g'h'", "abcdef'g'h'", "abcd'ef'g'h'", "abcd'ef'g'h", "ab'c'de'f'g'h'", "ab'c'd'e'f'g'h'"],["a'bcd'efgh", "a'bcd'efgh'", "abcdef'g'h"]))
print(comb_function_expansion(["ab'c'de'fgh'i'j'", "ab'c'de'fgh'ij", "ab'c'de'fgh'ij'", "ab'c'de'fghij", "ab'c'de'fghi'j", "a'b'c'def'gh'i'j'", "a'b'cdef'gh'i'j'", "a'bcd'ef'g'hij", "abc'd'e'fgh'ij", "abc'de'fgh'ij'"],["ab'c'de'fgh'i'j", "ab'c'de'fghij'", "ab'c'de'fghi'j'", "abc'de'fgh'ij", "abc'd'e'fgh'ij'"]))