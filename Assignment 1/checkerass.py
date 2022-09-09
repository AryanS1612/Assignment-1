def valid(term):
        universal = {0,1,2,3}
        gawd = [[{0,1},{2,3}],[{3,0},{1,2}]]
        set = universal
        if(len(term) == 2) :
                for i in range(len(term)):
                        if (term[i] != None):
                                set = set.intersection(gawd[i][term[i]])
                if(set == {0,3}):
                        return [3,0]
                return list(set)
        else:
                if(term[0] == None):
                        set = {0,1}
                else:
                        set = {term[0]}
                return list(set)

def is_legal_region(kmap_function,term):
        slice = int((len(term) - 1)/2)
        column = term[:slice+1];row = term[slice+1:]
        valid_column = valid(column);valid_row = valid(row)
        top_left = (valid_row[0],valid_column[0])
        bottom_right = (valid_row[len(valid_row)-1],valid_column[len(valid_column)-1])
        var = 0
        for i in valid_row:
                for j in valid_column:
                        if(kmap_function[i][j] == 0):
                                var += 1
        if(var > 0):
                return (top_left,bottom_right,False)
        else:
                return (top_left,bottom_right,True)

correct_ans = [((0, 0), (3, 3), False), ((1, 0), (2, 3), False), ((3, 0), (0, 3), False), ((2, 0), (3, 3), True), ((2, 0), (2, 3), True), ((3, 0), (3, 3), True), ((0, 0), (1, 3), False), ((1, 0), (1, 3), False), ((0, 0), (0, 3), False), ((0, 1), (3, 2), False), ((1, 1), (2, 2), True), ((3, 1), (0, 2), False), ((2, 1), (3, 2), True), ((2, 1), (2, 2), True), ((3, 1), (3, 2), True), ((0, 1), (1, 2), False), ((1, 1), (1, 2), True), ((0, 1), (0, 2), False), ((0, 3), (3, 0), False), ((1, 3), (2, 0), False), ((3, 3), (0, 0), True), ((2, 3), (3, 0), True), ((2, 3), (2, 0), True), ((3, 3), (3, 0), True), ((0, 3), (1, 0), False), ((1, 3), (1, 0), False), ((0, 3), (0, 0), True), ((0, 2), (3, 3), False), ((1, 2), (2, 3), True), ((3, 2), (0, 3), False), ((2, 2), (3, 3), True), ((2, 2), (2, 3), True), ((3, 2), (3, 3), True), ((0, 2), (1, 3), False), ((1, 2), (1, 3), True), ((0, 2), (0, 3), False), ((0, 2), (3, 2), False), ((1, 2), (2, 2), True), ((3, 2), (0, 2), False), ((2, 2), (3, 2), True), ((2, 2), (2, 2), True), ((3, 2), (3, 2), True), ((0, 2), (1, 2), False), ((1, 2), (1, 2), True), ((0, 2), (0, 2), False), ((0, 3), (3, 3), True), ((1, 3), (2, 3), True), ((3, 3), (0, 3), True), ((2, 3), (3, 3), True), ((2, 3), (2, 3), True), ((3, 3), (3, 3), True), ((0, 3), (1, 3), True), ((1, 3), (1, 3), True), ((0, 3), (0, 3), True), ((0, 0), (3, 1), False), ((1, 0), (2, 1), False), ((3, 0), (0, 1), True), ((2, 0), (3, 1), True), ((2, 0), (2, 1), True), ((3, 0), (3, 1), True), ((0, 0), (1, 1), False), ((1, 0), (1, 1), False), ((0, 0), (0, 1), True), ((0, 1), (3, 1), True), ((1, 1), (2, 1), True), ((3, 1), (0, 1), True), ((2, 1), (3, 1), True), ((2, 1), (2, 1), True), ((3, 1), (3, 1), True), ((0, 1), (1, 1), True), ((1, 1), (1, 1), True), ((0, 1), (0, 1), True), ((0, 0), (3, 0), False), ((1, 0), (2, 0), False), ((3, 0), (0, 0), True), ((2, 0), (3, 0), True), ((2, 0), (2, 0), True), ((3, 0), (3, 0), True), ((0, 0), (1, 0), False), ((1, 0), (1, 0), False), ((0, 0), (0, 0), True), ((0, 0), (1, 3), False), ((1, 0), (1, 3), False), ((0, 0), (0, 3), False), ((0, 1), (1, 2), False), ((1, 1), (1, 2), True), ((0, 1), (0, 2), False), ((0, 3), (1, 0), False), ((1, 3), (1, 0), False), ((0, 3), (0, 0), True), ((0, 2), (1, 3), False), ((1, 2), (1, 3), True), ((0, 2), (0, 3), False), ((0, 2), (1, 2), False), ((1, 2), (1, 2), True), ((0, 2), (0, 2), False), ((0, 3), (1, 3), True), ((1, 3), (1, 3), True), ((0, 3), (0, 3), True), ((0, 0), (1, 1), False), ((1, 0), (1, 1), False), ((0, 0), (0, 1), True), ((0, 1), (1, 1), True), ((1, 1), (1, 1), True), ((0, 1), (0, 1), True), ((0, 0), (1, 0), False), ((1, 0), (1, 0), False), ((0, 0), (0, 0), True), ((0, 0), (1, 1), False), ((1, 0), (1, 1), True), ((0, 0), (0, 1), False), ((0, 1), (1, 1), False), ((1, 1), (1, 1), True), ((0, 1), (0, 1), False), ((0, 0), (1, 0), True), ((1, 0), (1, 0), True), ((0, 0), (0, 0), True)]

k_map = [[1,'x',0,1],[0,1,1,1],['x',1,'x','x'],[1,1,1,'x']]
k_map1 = [[1,0],['x',1]]
lst = [None,1,0]
p = 0
a = []
check = True
for i in lst:
    for j in lst:
        for k in lst:
            for l in lst:
                if(is_legal_region(k_map,[i,j,k,l]) == correct_ans[p]) == False:
                    print([i,j,k,l])
                    if(check):
                        check = False
                p += 1

for i in lst:
    for j in lst:
        for k in lst:
            if(is_legal_region(k_map[:2],[i,j,k]) == correct_ans[p]) == False:
                    print([i,j,k])
                    if(check):
                        check = False
            p += 1

for i in lst:
    for j in lst:
        if(is_legal_region(k_map1,[i,j]) == correct_ans[p]) == False:
                    print([i,j])
                    if(check):
                        check = False
        p += 1

print(check)
