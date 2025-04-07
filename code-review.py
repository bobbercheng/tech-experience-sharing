"""
Given an array of integers nums and an integer target, return a list of unique triplets (a, b, c) such that a + b + c == target.

For example:

Given: nums = [0, 1, 2, 3, -1, 2], target = 2

Return: [(-1, 0, 3), (-1, 1, 2)]
Assume that 
1.  Triplets can be returned in any order.


"""



#======= Code snippet =======

def FindTriplets(nums, TARGET):
  ret = set()
  for i in range(0, len(nums)): # Loop through length of nums
    for j in range(i+1, len(nums)): # Loop through rest from i
      for k in range(j+1, len(nums)): # Loop through rest from j
        if (nums[i] + nums[j] + nums[k] == TARGET): # check if sum is the target
          ret.add(tuple([nums[i], nums[j], nums[k]])) # add to unique value to set
  return list(ret)

#===============================
print(FindTriplets([0, 1, 2, 3, -1, 2], 2))