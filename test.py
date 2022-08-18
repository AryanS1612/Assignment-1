# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 23:28:02 2022

@author: nsahu
"""

# from http.client import NotConnected
# from this import d
from operator import truediv
from K_map_gui_tk import *

"""
Class kmap is the wrapper for the tkinter gui.
Usage: kmap(<kmap values in list of list form>)
example for 2 input k-map, kmap([[1,0],[0,0]])
        for 3 input k-map, kmap([[1,0,0,1],[0,0,0,1]])
        for 4 input k-map, kmap([[1,0,0,1],[0,0,0,1],[0,1,0,1],[0,1,0,1]])

To draw the region, use api root.draw_region(x1,y1,x2,y2,"fill colour")
Here x1,y1 is the index for the top left corner of the region
x2,y2 is the index for the bottom right corner of the region.
Fill colour options = ['red', 'blue', 'green', 'yellow']
"""

"""
Sample code for the example given in the slide
"""

# root = kmap([[0,1,1,0], ['x',1,'x',0], [1,0,0,0], [1,'x',0,0]])
# root.draw_region(0,1,1,2,'blue')
# root.draw_region(3,3,0,0,'green')
# root.mainloop()


"""
Sample code for the displaying wrap region
"""
root = kmap([[0,1,1,0], ['x',1,'x',0], [1,0,0,0], [1,'x',0,0]])
#root.draw_region(1,3,2,0,'blue')
root.draw_region(3,0,0,3,'green')
root.mainloop()

def solve(term):
        seta0 = {0,1};seta1 = {2,3};setb0 = {3,0};setb1 = {1,2};universal = {0,1,2,3}
        lst0 = [];lst1 = [];gawd = []
        lst0.append(seta0);lst0.append(seta1)
        lst1.append(setb0);lst1.append(setb1)
        gawd.append(lst0);gawd.append(lst1)
        set = universal
        if(len(term) == 2) :
                for i in range(len(term)):
                        if (term[i] != NONE):
                                set = set.intersection(gawd[i][term[i]])
                if(set == {0,3}):
                        return [3,0]
                return list(set)
        else:
                if(term[0] == NONE):
                        set = {0,1}
                else:
                        set = {term[0]}
                return list(set)

def is_legal_region(kmap_function,term):
        variables = len(term)
        split = int((variables - 1)/2)
        set1 = {}
        column = term[0:split+1]
        row = term[split+1:]
        setcolumn = solve(column)
        setrow = solve(row)
        print(setcolumn)
        print(setrow)
        top_left = (setrow[0],setcolumn[0])
        bottom_right = (setrow[len(setrow)-1],setcolumn[len(setcolumn)-1]);var1 = 0
        for i in setrow:
                for j in setcolumn:
                        if(kmap_function[i][j] == 1):
                                var1 += 1
        if(var1 > 0):
                return (top_left,bottom_right,False)
        else:
                return (top_left,bottom_right,True)

print(is_legal_region([[0,1,1,0], ['x',1,'x',0], [1,0,0,0], [1,'x',0,0]],[NONE,NONE,NONE,NONE]))