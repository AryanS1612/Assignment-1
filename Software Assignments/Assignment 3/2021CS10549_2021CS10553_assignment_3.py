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

# print(opt_function_reduce(["a'b'c'", "a'b'c", "a'bc'", "ab'c", "abc'", "abc"],[]))
# print(opt_function_reduce(["a'b'c'd'", "a'b'cd'", "a'b'cd", "a'bc'd", "a'bcd'", "a'bcd", "ab'c'd'", "ab'c'd", "ab'cd'", "abc'd'", "abcd'", 'abcd'],[]))

# from cmath import inf
# from pickle import NONE
# from re import A
# from tkinter import N
# from operator import truediv
# import K_map_gui_tk
# from K_map_gui_tk import kmap
# import test
# from test import is_legal_region

# def custom_print(groups,n):
#     it = 0
#     Empty = (None,'{}')
#     if(len(groups)==0):
#         print("Terms of the answer after this iteration are :")
#         print(Empty)
#     elif((type(groups[0]) == tuple)):
#         print("Terms of the answer after this iteration are :")
#         for i in groups:
#             decoded = fromBinary(i[0],i[1],n)
#             terms = set()
#             for k in i[2]:
#                 terms.add(fromBinary(k,0,n))
#             final = (decoded,terms)
#             print("     ",final)
#     else:
#         for i in groups:
#             print("Group number",it)
#             if(len(i) == 0):
#                 print("     ",Empty)
#             else:
#                 for j in i:
#                     decoded = fromBinary(j[0],j[1],n)
#                     terms = set()
#                     for k in j[2]:
#                         terms.add(fromBinary(k,0,n))
#                     final = (decoded,terms)
#                     print("     ",final)
#             it += 1

# def toBinary(str):
#     bin,cb = 0,0
#     for i in range(0, len(str)):
#         if(str[i].isalpha()):
#             if(i+1>=len(str)): cb=1
#             elif(str[i+1] == '\''): cb=0
#             else: cb=1
#             bin = bin*2+cb
#     return bin

# def fromBinary(nbin,dbin,n):
#     bins = bin(nbin)[2:]
#     dbins = bin(dbin)[2:]
#     ch = 97+n-1
#     lst=[]
#     for i in range (0,len(bins)):
#         if(i<len(dbins)):
#             if(dbins[len(dbins)-i-1] == '1'): 
#                 ch-=1
#                 continue
#             elif(bins[len(bins)-i-1] == '1'): lst.append(chr(ch))
#             elif(bins[len(bins)-i-1] == '0'): lst.append(chr(ch)+"'")
#         else:
#             if(bins[len(bins)-1-i] == '1'): lst.append((chr(ch)))
#             elif(bins[len(bins)-1-i] == '0'): lst.append((chr(ch))+"'")
#         ch-=1
#     for i in range(len(bins),n):
#         lst.append(chr(ch)+"'")
#         ch-=1
#     lst.reverse()
#     str = ''.join(lst)
#     return str

# def combine(group,ans,n):
#     groups = [ [] for _ in range(len(group)-1) ]
#     set1,set2 = set(),set()
#     for i in range(0, len(group)-1):
#         for j in range(0, len(group[i])):
#             check = False
#             for k in range(0, len(group[i+1])):
#                 if(group[i][j][1] == group[i+1][k][1]):
#                     tset = set()
#                     xor = group[i][j][0] ^ group[i+1][k][0]
#                     if((xor&(xor-1)) == 0):
#                         b = xor.bit_length()
#                         y = group[i+1][k][0]
#                         tset = tset.union(group[i][j][2])
#                         tset = tset.union(group[i+1][k][2])
#                         set2.add((group[i+1][k][0],group[i+1][k][1]))
#                         check = True
#                         index = bin(y).count("1")-bin(xor+group[i][j][1]).count("1") 
#                         groups[index].append((y,xor+group[i][j][1],tset))
#             if(check == False): 
#                 if(((group[i][j][0],group[i][j][1]) in set1) == False): ans.append(group[i][j])
#         set1 = set2
#         set2 = set()
#     x = len(group) - 1
#     for i in range(len(group[len(group)-1])):
#         if(((group[x][i][0],group[x][i][1]) in set1) == False): ans.append(group[x][i])
#     final = True
#     for i in groups:
#         if(len(i) != 0): final = False
#     # custom_print(ans,n)
#     # print()
#     # print('New iteration')
#     # print("printing groups")
#     # custom_print(groups,n)
#     if(final): return ans
#     else: return combine(groups,ans,n)

# def comb_function_expansion(func_TRUE, func_DC):
#     """
#     determines the maximum legal region for each term in the K-map function
#     Arguments:
#     func_TRUE: list containing the terms for which the output is '1'
#     func_DC: list containing the terms for which the output is 'x'
#     Return:
#     a list of terms: expanded terms in form of boolean literals
#     """
#     n = 0
#     dict,count = {},{}
#     for ch in func_TRUE[0]:
#         if(ch.isalpha()): n+=1
#     groups = [ [] for _ in range(n+1) ]
#     truebin, dcbin = [],[]
#     it = 0
#     for each in func_TRUE:
#         binary = toBinary(each)
#         truebin.append(binary)
#         groups[bin(binary).count("1")].append((binary,0,{binary}))
#         dict[binary] = it
#         count[binary] = 0
#         it += 1
#     truesize = it
#     for each in func_DC:
#         binary = toBinary(each)
#         dcbin.append(binary)
#         groups[bin(binary).count("1")].append((binary,0,{binary}))
#         dict[binary] = it
#         count[binary] = 0
#         it += 1
#     ans = combine(groups,[],n)
#     ans.sort(key = lambda x: -len(x[2]))
#     output = [ None for _ in range(it)]
#     completeset = set()
#     for each in ans:
#         nonset = each[2] - completeset
#         for element in nonset:
#             output[dict[element]] = each
#         completeset = completeset.union(nonset)
#     for i in ans:
#         for j in i[2]:
#             count[j] += 1
#     list = []
#     it = 0
#     truebin += dcbin
#     for i in truebin:
#         list.append([count[i],i,it])
#         it += 1
#     length = it
#     finalans = []
#     for i in list:
#         it =0
#         min = list[0][0]
#         for j in range(1,length):
#             if(list[j][0] < min):
#                 min = list[j][0]
#         if(min == inf):
#             break
#         for j in range(length):
#             if(list[j][0] == min):
#                 if(j in dcbin):
#                     dcbin.remove
#                     list[j][0] = inf
#                     continue
#                 index = j
#                 break
#         for each in output[list[index][2]][2]:
#             list[dict[each]][0] = inf
#         finalans.append(output[list[index][2]])
#     for i in range(len(finalans)):
#         finalans[i] = fromBinary(finalans[i][0],finalans[i][1],n)
#     return finalans

# print(opt_function_reduce(["abc'd'", "a'b'c'd", "abc'd", "ab'cd", "a'bcd'"],["a'bc'd", "a'bcd", "abcd"]))
# print(opt_function_reduce(["ab'c'd'", "abc'd", "ab'c'd", "a'bcd", "abcd", "a'b'cd'", "a'bcd'"],[]))
# print(opt_function_reduce(["a'b'c'd'e'f'", "a'b'c'd'ef'", "a'b'c'd'ef", "a'b'c'de'f", "a'bc'def", "a'bc'd'ef", "a'bcd'ef'", "a'bcd'e'f'", "a'bcde'f'", "a'b'cd'e'f", "a'b'cde'f", "ab'cd'e'f", "abcde'f", "ab'cd'ef", "abcd'ef'", "abc'd'ef'", "ab'c'd'e'f'", "ab'c'de'f'"],["a'b'c'd'e'f", "a'bc'de'f", "a'bc'd'e'f", "a'bcdef'", "abcd'e'f'", 'abcdef', "ab'c'd'ef'", "ab'c'def'", "abc'd'e'f'"]))
# print(opt_function_reduce( ["a'b'c'de'fg'h", "a'bc'de'f'g'h'", "a'b'c'de'fgh", "a'bc'de'f'gh'", "a'b'c'defgh", "a'bc'def'gh'", "a'b'c'defg'h", "a'bc'def'g'h'", "ab'cd'e'f'gh", "ab'cd'e'fgh", "ab'cd'e'fgh'", "ab'cde'fgh'", "ab'cd'ef'gh", "ab'cd'efgh", "ab'cd'efgh'", "ab'cdefgh'", "ab'cd'ef'g'h", "ab'cd'efg'h", "ab'cd'efg'h'", "ab'cdefg'h'", "ab'c'd'ef'g'h", "ab'c'd'efg'h", "ab'c'd'efg'h'", "ab'c'defg'h'", "abcde'f'gh", "abcde'fgh", "abcde'fgh'", "abcd'e'fgh'", "abcdef'gh", 'abcdefgh', "abcdefgh'", "abcd'efgh'", "abcdef'g'h", "abcdefg'h", "abcdefg'h'", "abcd'efg'h'", "abc'def'g'h", "abc'defg'h", "abc'defg'h'", "abc'd'efg'h'"], []))