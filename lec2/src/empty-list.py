#!/usr/bin/env python

def remove_empty_lists(input_list):
    tmp = []

    for x in input_list:
        if x != []:
            tmp.append(x)
            
    i = 0
    while i < len(tmp):
        input_list[i] = tmp[i]
        i += 1
        
    while i < len(input_list):
        del(input_list[-1])
        
input = [3, 11, [4,3], [], 4, [1], 18]
remove_empty_lists(input)
print(input)
