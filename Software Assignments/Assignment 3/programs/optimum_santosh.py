# A class used to represent a region consisting of one or more cells
# It allows to increase efficiency as minterms joined to create region are also stored
class Term:
    def __init__(self,minterms,boollist):
        self.minterms = minterms
        self.boollist = boollist
        self.used = False

        self.minterms.sort()

    # string representation of the class
    def __str__(self):
        alpha = ''
        for i in self.minterms:
            alpha += str(i) + ' '
        return alpha
    
    # equality operator for the class
    def __eq__(self,term):
        if term == None:
            if self.minterms:
                return False
            return True
        elif self.boollist == term.boollist and self.minterms == term.minterms:
            return True
    
    # method to mark an object of the class as used
    def use(self):
        self.used = True


# helper function to combine two terms 1 and 2
# If combination is possible the output is returned
# If not then None is returned
def combine(term1,term2):

    # checking if the terms are the same
    if term1.boollist == term2.boollist:
        return None
    
    # A variable 'diff' to represent number of different truth values
    diff = 0
    result = []

    # looping over the length of the terms to compare and increase 'diff'
    for i in range(len(term1.boollist)):

        # Updating the value of diff and simultaneously creating the output
        if term1.boollist[i] != term2.boollist[i]:
            diff += 1
            result.append(None)
        
        else:
            result.append(term1.boollist[i])
        
        # Combination is not possible
        if diff > 1:
            return None
    
    # returning the result as combination is possible if we reach here
    return Term(term1.minterms + term2.minterms,result)


# Helper function to convert strings of literals into an object of above class Term of exactly one cell
def lit_to_bool(literals,numofvar):
    boollist = [1]*numofvar

    varcount = -1

    # loop over string and get 0 or 1 by checking for ' after each literal
    for j in range(len(literals)):
        if (literals[j] == '\''):
            boollist[varcount] = 0
        else:
            varcount += 1

    value = 0
    multiplier = 1

    # Get the minterm number corresponding to the cell
    for i in range(len(boollist)-1,-1,-1):
        value += boollist[i]*multiplier
        multiplier *= 2
        
    return Term([value],boollist)


# A function to revert back the list into a string of literals
def bool_to_lit(minterm,literals):
    term = ''
    length = len(literals)

    # loop over boollist of term to add literal to string
    for i in range(length):
        if (minterm.boollist[i] != None):
            term = term + literals[i]

            if (minterm.boollist[i] == 0):
                term = term + '\''

    # If the term is empty that is all 'None's then we return None
    if(term==''):
        return None

    return term

# Helper function to create initial 2-D list
# It appends into list at position chosen by number of 1s in the term
def initial_grouping(numofvar,truetermlist):

    groups = []

    # Create 2-D list containing empty lists
    for count in range(numofvar + 1):
        groups.append([])
    
    # Loop over the terms in input and append into 2-D list
    for trueterm in truetermlist:

        count = 0
        for i in trueterm.boollist:
            if i == 1:
                count += 1

        groups[count].append(trueterm)
    
    return groups


def opt_function_reduce(func_TRUE,func_DC):

    # If input is has no 1s then return
    if func_TRUE == []:
        return []
    
    firstterm = func_TRUE[0]
    numofvar = 0
    variables = []

    # loop to find the number of literals or variables
    for i in firstterm:
        if (i != '\''):
            numofvar += 1
            variables.append(i)

    truetermlist = []
    DCminterms=[]

    # Adding true terms to the above true term list
    for i in func_TRUE:
        boolterm = lit_to_bool(i,numofvar)
        truetermlist.append(boolterm)
    
    # Adding DC terms as well by considering them to be true for now
    # Keeping track of DC minterms in another list
    for i in func_DC:
        boolterm = lit_to_bool(i,numofvar)
        truetermlist.append(boolterm)
        DCminterms += boolterm.minterms


    # Helper function to get all the prime implicants
    # Prime implicants represent regions which are maximally expanded
    def get_prime_implicants(groups = None):

        # Precaution to handle faulty input
        if groups == None:
            groups = initial_grouping(numofvar,truetermlist)
        
        # If size of groups is 1 then we can directly return its first term
        length = len(groups)
        if length == 1:
            return groups[0]
        
        else:
            unused = []
            new_groups = []

            # Creation of 2d list in new_groups
            for i in range(length-1):
                new_groups.append([])

            # Loop over 2d list 'groups'
            # Consider consecutive lists present in 'groups' in each iteration
            for j in range(length-1):
                group1 = groups[j]
                group2 = groups[j+1]

                # Loop over the terms of the current consecutive groups
                for term1 in group1:
                    for term2 in group2:
                        
                        # Check if current two terms can be combined
                        term3 = combine(term1,term2)

                        # If combination is possible then mark the terms as used
                        if term3 != None:
                            term1.use()
                            term2.use()
                            
                            # Add the combined term to new_groups if not already present
                            if term3 not in new_groups[j]:
                                new_groups[j].append(term3)

            # Loop over groups to retrieve all the unused terms
            for group in groups:
                for term in group:
                    if not term.used and term not in unused:
                        unused.append(term)

            # Recurse over the same function with parameter new_groups
            # new_groups basically represents the combination of regions which got used
            # We keep recursing to get all the unused terms
            for term in get_prime_implicants(new_groups):
                if not term.used and term not in unused:
                    unused.append(term)
                
            return unused
    
    # Calling the above function to get the prime implicants
    prime_imp=get_prime_implicants(initial_grouping(numofvar,truetermlist))
    dict={}

    # Looping over the prime implicants to create a dict
    # This dict will map each minterm number to a list of regions
    # The list will contain all prime implicants which have the minterm
    for i in range(len(prime_imp)):
        minlist=prime_imp[i].minterms

        # Looping over the minterms and checking/updating the dict
        for j in minlist:
            if(j not in dict):
                dict[j]=[prime_imp[i]]
            else:
                dict[j].append(prime_imp[i])
 
    essentialprimeimp=[]

    # Looping over the prime implicants
    for i in range(len(prime_imp)):
        cells=prime_imp[i].minterms

        # An indicator to see if the prime implicant is essential
        indicator=0

        # Loop over the cells of the current prime implicant
        for j in range(len(cells)):

            # If the count of regions containing is 1 and the cell is not DC
            # We append it to essential prime implicants list
            if(len(dict[cells[j]])==1 and cells[j] not in DCminterms):
                indicator=1
                essentialprimeimp.append(bool_to_lit(prime_imp[i],variables))
                break
        
        # We check if the indicator is zero
        # This would imply that the current prime implicant is not essential
        # We update the dict accordingly by removing this region
        if(indicator==0):
            # print("Deleted term:",bool_to_lit(prime_imp[i],variables))

            # Looping over the cells to remove the current prime implicant from dict
            for j in range(len(cells)):
                dict[cells[j]].remove(prime_imp[i])

    return essentialprimeimp

print(opt_function_reduce(["ab'c'de'fgh'i'j'", "ab'c'de'fgh'ij", "ab'c'de'fgh'ij'", "ab'c'de'fghij", "ab'c'de'fghi'j", "a'b'c'def'gh'i'j'", "a'b'cdef'gh'i'j'", "a'bcd'ef'g'hij", "abc'd'e'fgh'ij", "abc'de'fgh'ij'"],["ab'c'de'fgh'i'j'", "ab'c'de'fgh'ij", "ab'c'de'fgh'ij'", "ab'c'de'fghij", "ab'c'de'fghi'j", "a'b'c'def'gh'i'j'", "a'b'cdef'gh'i'j'", "a'bcd'ef'g'hij", "abc'd'e'fgh'ij", "abc'de'fgh'ij'"]))