def split_array(nums, k):
    """
    Split nums into k subarrays while minimizing the largest sum of any subarray.
    
    Args:
        nums: List[int] - The array to split
        k: int - Number of subarrays to split into
    
    Returns:
        int - The minimized largest sum after splitting
    """
    # Binary search solution
    # The minimum possible result is the max value in the array
    # The maximum possible result is the sum of all elements
    left = max(nums)
    right = sum(nums)
    
    # Binary search for the minimum possible maximum subarray sum
    while left < right:
        mid = (left + right) // 2
        
        # Check if we can split the array into k or fewer subarrays
        # with the maximum sum being mid
        if can_split(nums, k, mid):
            right = mid
        else:
            left = mid + 1
    
    return left

def can_split(nums, k, max_sum):
    """
    Check if we can split nums into k or fewer subarrays with maximum sum max_sum.
    
    Args:
        nums: List[int] - The array to split
        k: int - Maximum number of subarrays
        max_sum: int - Maximum sum allowed for any subarray
    
    Returns:
        bool - Whether it's possible to split the array as required
    """
    count = 1  # Start with one subarray
    current_sum = 0
    
    for num in nums:
        # If adding the current number exceeds max_sum,
        # we need to start a new subarray
        if current_sum + num > max_sum:
            count += 1
            current_sum = num
            
            # If we need more than k subarrays, return False
            if count > k:
                return False
        else:
            current_sum += num
    
    # We were able to split into k or fewer subarrays
    return True

# Test with examples
if __name__ == "__main__":
    print(split_array([7, 2, 5, 10, 8], 2))  # Expected: 18
    print(split_array([1, 2, 3, 4, 5], 2))   # Expected: 9 