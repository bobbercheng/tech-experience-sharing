"""
The solution to "Shortest Subarray with Sum at Least K" works through these key concepts:
Prefix Sums: We create an array where each position holds the sum of all elements up to that point. This lets us calculate any subarray sum as prefix_sum[end+1] - prefix_sum[start].
Monotonic Deque: We use a double-ended queue to track promising starting positions for subarrays:
We maintain indices in the deque so their corresponding prefix sums are in increasing order
This is crucial because if we have two potential starts j1 < j2 where prefix_sum[j1] ≥ prefix_sum[j2], the j2 starting position will always give us a shorter valid subarray
Two-step Process for each position i:
First, we check if current prefix sum minus any prefix sum at the deque front is ≥ k. If so, we've found a valid subarray and update our result.
Second, we remove any indices from the back of the deque whose prefix sums are ≥ current prefix sum (they can't lead to shorter valid subarrays).
Example: For [2,-1,2] with k=3:
Prefix sums: [0,2,1,3]
When we reach prefix_sum[3]=3, we find prefix_sum[3]-prefix_sum[0]=3 ≥ k
This gives us a subarray of length 3, which is our answer
This achieves O(n) time complexity, far better than the naive O(n²) approach.
"""

from collections import deque

def shortestSubarray(nums, k):
    n = len(nums)
    
    # Create prefix sum array
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    # Initialize result with a value larger than any possible subarray length
    result = n + 1
    
    # Use a deque to maintain a monotonically increasing prefix sum
    monoq = deque()
    
    for i in range(n + 1):
        # For each prefix_sum[i], find the earliest prefix_sum[j] such that
        # prefix_sum[i] - prefix_sum[j] >= k
        while monoq and prefix_sum[i] - prefix_sum[monoq[0]] >= k:
            result = min(result, i - monoq.popleft())
        
        # Remove all prefix sums that are larger than current
        # because they won't lead to a shorter subarray
        while monoq and prefix_sum[i] <= prefix_sum[monoq[-1]]:
            monoq.pop()
        
        monoq.append(i)
    
    return result if result <= n else -1

# Test cases
print(shortestSubarray([1], 1))  # Expected: 1
print(shortestSubarray([1, 2], 4))  # Expected: -1
print(shortestSubarray([2, -1, 2], 3))  # Expected: 3 