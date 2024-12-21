#!/usr/bin/env python

def rotations(nums):
    lx, rx = 0, len(nums)-1
    while lx <= rx:
        if nums[lx] <= nums[rx]:
            return lx

        cx = int((lx+rx)/2)
        
        if cx == len(nums)-1:
            next = 0
        else:
            next = cx + 1

        if cx == 0:
            prev = len(nums)-1
        else:
            prev = cx - 1

        # next = (cx + 1) % len(nums)
        # prev = (cx - 1 + len(nums)) % len(nums)

        if nums[cx] < nums[next] and nums[cx] < nums[prev]:
            return cx

        if nums[cx] <= nums[rx]:
            rx = cx - 1
        else:
            lx = cx + 1
 
nums = [7,7,7,8, 2,2,2,2,2,2,2,2,2,2]
print(f'The list is rotated {rotations(nums)} times')
