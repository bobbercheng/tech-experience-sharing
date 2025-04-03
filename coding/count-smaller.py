"""
The "Count of Smaller Numbers After Self" problem can be solved using several approaches:
Brute Force (O(n²)): Use nested loops to count smaller elements to the right. Simple but too slow for the given constraints (up to 10^5 elements).
Binary Search Tree (O(n log n) average, O(n²) worst): Traverse right-to-left, inserting elements into a BST that tracks smaller elements. Efficient in average case but can degrade to O(n²) with skewed inputs.
Segment/Fenwick Tree (O(n log n)): Use specialized data structures to track frequency of elements in ranges. Efficient but complex to implement.
Balanced BST (O(n log n)): Similar to regular BST but guarantees log(n) operations by maintaining balance. Complicated to implement correctly.
Merge Sort (O(n log n)): The implemented solution, which is ideal because:
It guarantees O(n log n) time complexity in all cases
It's relatively simple to implement
During merging, we naturally count smaller elements to the right
The key insight: when merging sorted subarrays, if we take an element from the left subarray, all elements already taken from the right subarray are smaller than it and were originally to its right
The merge sort approach elegantly combines sorting with counting while maintaining the original indices. The variable j tracks how many elements from the right subarray have been processed, which directly corresponds to smaller elements originally to the right.
This approach provides the best balance of efficiency, simplicity, and robustness for this particular problem.
"""
def countSmaller(nums: list[int]) -> list[int]:
    # Edge case
    if not nums:
        return []
    
    # Create a list of tuples (value, original index)
    indexed_nums = [(nums[i], i) for i in range(len(nums))]
    result = [0] * len(nums)
    
    # Merge sort function that also counts smaller numbers
    def merge_sort(arr: list[tuple[int, int]]) -> list[tuple[int, int]]:
        if len(arr) <= 1:
            return arr
        
        # Divide array in half
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        
        # Merge and count
        return merge(left, right)
    
    def merge(left: list[tuple[int, int]], right: list[tuple[int, int]]) -> list[tuple[int, int]]:
        merged = []
        i, j = 0, 0
        
        while i < len(left) and j < len(right):
            # If right element is smaller, increment count
            if left[i][0] > right[j][0]:
                merged.append(right[j])
                j += 1
            else:
                # Update result - add count of elements from right
                # that are smaller than current left element
                result[left[i][1]] += j
                merged.append(left[i])
                i += 1
        
        # Handle remaining elements
        while i < len(left):
            result[left[i][1]] += j  # All right elements are smaller
            merged.append(left[i])
            i += 1
        
        while j < len(right):
            merged.append(right[j])
            j += 1
            
        return merged
    
    merge_sort(indexed_nums)
    return result

# Test cases
print(countSmaller([5,2,6,1]))  # Expected: [2,1,1,0]
print(countSmaller([-1]))      # Expected: [0]
print(countSmaller([-1,-1]))   # Expected: [0,0] 