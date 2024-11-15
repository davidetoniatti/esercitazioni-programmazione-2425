#!/usr/bin/env python

def find_smallest_missing(nums):
    n = len(nums)
    lx, rx = 0, n-1

    while lx <= rx:
        cx = int((lx+rx)/2)
        if cx == nums[cx]:
            lx = cx+1
        else:
            rx = cx - 1

    return lx
"""
Sia n la lunghezza della lista.
Complessità temporale: O(log n)
Complessità spaziale: O(1)
"""

print(find_smallest_missing([1,2,6,7,10,11,13]))
