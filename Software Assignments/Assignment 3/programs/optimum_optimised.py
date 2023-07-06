import math
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
    global n
    n=0
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
        dict[binary] = it
        count[binary] = 0
        it += 1
    truesize = it
    for each in func_DC:
        binary = toBinary(each)
        dcbin.append(binary)
        groups[bin(binary).count("1")].append((binary,0,{binary}))
        dict[binary] = it
        count[binary] = 0
        it += 1
    # print("printing groups")
    # custom_print(groups,n)
    ans = combine(groups,[],n)
    ans.sort(key = lambda x: -len(x[2]))
    output = []
    ans = combine(groups,[],n)
    ans.sort(key = lambda x: -len(x[2]))
    # print(ans)
    output = []
    check = {}
    for i in ans:
        check[(i[0],i[1])] = 0
    for i in ans:
        check[(i[0],i[1])] += 1
    for i in ans:
        if(check[(i[0],i[1])] > 1):
            check[(i[0],i[1])] -= 1
        else:
            output.append(i)
    output[::-1]
    return output

def opt_function_reduce(func_TRUE, func_DC):
    """
    determines the minimum number of sum of product terms for the given K-map function
    Arguments:
    func_TRUE: list containing the terms for which the output is '1'
    func_DC: list containing the terms for which the output is 'x'
    Return:
    a list of minimum size containing terms: terms in form of boolean literals
    """
    dcbin = []
    for each in func_DC:
        binary = toBinary(each)
        dcbin.append(binary)
    primeimp = comb_function_expansion(func_TRUE, func_DC)
    dict1 = {}
    finalans = []
    for i in range (0, len(primeimp)):
        for each in primeimp[i][2]:
            if(each in dcbin):
                continue
            if(each in dict1):
                dict1[each].append(primeimp[i])
            else:
                dict1[each] = []
                dict1[each].append(primeimp[i])
    for each in list(dict1):
        if(each not in dict1): continue
        if(len(dict1[each]) == 1):
            finalans.append(dict1[each][0])
            for key in dict1[each][0][2]:
                dict1.pop(key, None)
    petrick = []
    dict2 = {}
    i = 1
    ch = False
    if(dict1 == {}):
        output=[]
        for each in finalans:
            output.append(fromBinary(each[0],each[1],n))
        return output
    for each in dict1:
        newlst = []
        for lst in dict1[each]:
            for keys in dict2:
                if(dict2[keys] == lst):
                    newlst.append(keys)
                    ch = True
                    break
            if(ch == False): 
                dict2[i] = lst
                newlst.append(i)
                i*=2
            ch = False
        petrick.append(newlst)
    for i in range(1, len(petrick)):
        newlst = []
        for j in range(len(petrick[i])):
            for k in range(len(petrick[i-1])):
                newlst.append(petrick[i-1][k] | petrick[i][j])
        petrick[i] = newlst
    min = 0
    for i in range(1, len(petrick[len(petrick)-1])):
        if(bin(petrick[len(petrick)-1][i]).count("1") < bin(petrick[len(petrick)-1][min]).count("1")): min=i
    # for each in petrick[len(petrick)-1][min]:
    x = bin(petrick[len(petrick)-1][min])[2:]
    length = len(x)
    i = 0
    y = x[::-1]
    while(i < length):
        if(y[i] == '1'):
            finalans.append(dict2[(1<<(i))])
        i += 1
    output = []
    for each in finalans:
        output.append(fromBinary(each[0],each[1],n))
    return output

def convert(a,n):
    lst = [None]*n
    i = 0
    length = len(a)
    while(i < length):
        x = ord(a[i])
        if(i != length -1):
            if(a[i+1] == '\''):
                lst[x-97] = 0
                i += 2
            else:
                lst[x-97] = 1
                i += 1
        else:
            lst[x-97] = 1
            i += 1
    return lst
        
def convert_func(true,DC):
    n = int(math.log(len(true),2))
    func_TRUE = []
    func_DC = []
    it = 0
    for i in true:
        if(i == '0'):
            func_TRUE.append(fromBinary(it,0,n))
            # print(fromBinary(it,0,n))
        it += 1
    it = 0
    for i in DC:
        if(i == '1'):
            func_DC.append(fromBinary(it,0,n))
        it += 1
    # print(func_TRUE)
    # print(func_DC)
    return opt_function_reduce(func_TRUE,func_DC) 
# def gui_regions(func_TRUE,func_DC,ans_lst,num_col):
#     color_list = ['red','green','yellow','blue','orange','violet']
#     n = len(ans_lst[0])
#     row = pow(2,int((n-1)/2))
#     column = pow(2,int((n+1)/2))
#     lst = [[]]*column

# print(opt_function_reduce(["a'b'c'd", "a'b'cd", "a'bc'd", "abc'd'", "abc'd", "ab'c'd'", "ab'cd"], ["a'bc'd'","a'bcd", "ab'c'd"]))
# print(opt_function_reduce(["a'b'c'", "a'b'c", "a'bc'", "ab'c", "abc'", "abc"],[]))
# print(opt_function_reduce(["a'b'cd'","a'b'cd","a'bcd","ab'c'd","ab'cd","abc'd"],["a'b'c'd","ab'cd'","abcd"]))
# print(opt_function_reduce(["ab'c'de","ab'cde","abcde"],["a'bcd'e'","a'bcde'","a'bcd'e","a'bcde","abc'de"]))
# print(opt_function_reduce(["ab'c'de'fgh'i'j'", "ab'c'de'fgh'ij", "ab'c'de'fgh'ij'", "ab'c'de'fghij", "ab'c'de'fghi'j", "a'b'c'def'gh'i'j'", "a'b'cdef'gh'i'j'", "a'bcd'ef'g'hij", "abc'd'e'fgh'ij", "abc'de'fgh'ij'"],["ab'c'de'fgh'i'j'", "ab'c'de'fgh'ij", "ab'c'de'fgh'ij'", "ab'c'de'fghij", "ab'c'de'fghi'j", "a'b'c'def'gh'i'j'", "a'b'cdef'gh'i'j'", "a'bcd'ef'g'hij", "abc'd'e'fgh'ij", "abc'de'fgh'ij'"]))
# ans = opt_function_reduce(["a'b'cd'","a'b'cd","a'bcd","ab'c'd","ab'cd","abc'd"],["a'b'c'd","ab'cd'","abcd"])
# print(opt_function_reduce(["a'b'c'd'", "a'b'cd'", "a'b'cd", "a'bc'd", "a'bcd'", "a'bcd", "ab'c'd'", "ab'c'd", "ab'cd'", "abc'd'", "abcd'", 'abcd'],[]))
# print(convert_func("1011011111101011","0000000000000000"))
# print(convert_func("1111100111100100","0000000000000000"))
# print(convert_func("1101111111110100","0000000000000000"))
# print(convert_func("1011011011011110","0000000000000000"))
# print(convert_func("1010001010111111","0000000000000000"))
# print(convert_func("1000111011111011","0000000000000000"))
# print(convert_func("0011111011110111","0000000000000000"))
# m = int(input())
# ans = opt_function_reduce(["a'b'c'", "a'b'c", "a'bc'", "ab'c", "abc'", "abc"],[])
# print(ans)
# k_map = [[1,1,0,1],[0,1,1,1]]
# # k_map = [[0,0,0,0],['x',0,1,1],[1,1,'x',1],[1,0,0,'x']]
# root = kmap(k_map)
# it =0
# for i in ans:
#     term = convert(i,m)
#     a = is_legal_region(k_map,term)
#     if(it%3 == 0):
#         root.draw_region(a[0][0],a[0][1],a[1][0],a[1][1],'red')
#     elif(it%3 == 1):
#         root.draw_region(a[0][0],a[0][1],a[1][0],a[1][1],'green')
#     else:
#         root.draw_region(a[0][0],a[0][1],a[1][0],a[1][1],'blue')
#     it += 1
# root.mainloop()