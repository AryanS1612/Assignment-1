from cmath import inf
from pickle import NONE
from queue import PriorityQueue
from re import A

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
    dict,count = {},{}
    for ch in func_TRUE[0]:
        if(ch.isalpha()): n+=1
    groups = [ [] for _ in range(n+1) ]
    truebin, dcbin = [],[]
    it = 0
    for each in func_TRUE:
        binary = toBinary(each)
        truebin.append(binary)
        groups[bin(binary).count("1")].append((binary,0,{binary}))
        dict[binary] = (it,True)
        count[binary] = [0,[]]
        it += 1
    truesize = it
    for each in func_DC:
        binary = toBinary(each)
        dcbin.append(binary)
        groups[bin(binary).count("1")].append((binary,0,{binary}))
        dict[binary] = (it,False)
        count[binary] = [0,[]]
        it += 1
    # print("printing groups")
    # custom_print(groups,n)
    # print(truebin)
    # print(dcbin)
    ans = combine(groups,[],n)
    ans.sort(key = lambda x: -len(x[2]))
    # print(ans)
    output = []
    check = False
    for j in ans[0][2]:
        if (dict[j][1] == True):
            check = True
            break
    if(check):
            output.append(ans[0])
    for i in range(1,len(ans)):
        if(ans[i][2] != ans[i-1][2]):   
            check = False
            for j in ans[i][2]:
                if (dict[j][1] == True):
                    check = True
                    break
            if(check):
                output.append(ans[i])
    output[::-1]
    print(output)
    finalans = []
    
    # for i in range(len(finalans)):
    #     finalans[i] = fromBinary(finalans[i][0],finalans[i][1],n)
    # return finalans

# print(comb_function_expansion(["a'bc'd'", "abc'd'", "a'b'c'd", "a'bc'd", "a'b'cd"],["abc'd"]))
# print(comb_function_expansion(["a'b'c'd", "a'b'cd", "a'bc'd", "abc'd'", "abc'd", "ab'c'd'", "ab'cd"],["a'bc'd'", "a'bcd", "ab'c'd"]))
# print(comb_function_expansion(["a'b'c'd'e'", "a'bc'd'e'", "abc'd'e'", "ab'c'd'e'", "abc'de'", "abcde'","a'bcde'", "a'bcd'e'", "abcd'e'", "a'bc'de", "abc'de", "abcde","a'bcde", "a'bcd'e", "abcd'e", "a'b'cd'e", "ab'cd'e"],[]))
# print(comb_function_expansion(["a'b'c'd'","a'bc'd'","ab'c'd'","a'bc'd","abc'd","ab'c'd","a'b'cd","a'bcd","abcd","a'b'cd'","abcd'","ab'cd'"],[]))
# print(comb_function_expansion(["ab","a'b'","ab'","a'b"],[]))
# print(comb_function_expansion(["ab'c'de","ab'cde","abcde"],["a'bcd'e'","a'bcde'","a'bcd'e","a'bcde","abc'de"]))
# print(comb_function_expansion(["a'b'cd'","a'b'cd","a'bcd","ab'c'd","ab'cd","abc'd"],["a'b'c'd","ab'cd'","abcd"]))