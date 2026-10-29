class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Understand
        Input - Array, target int 
        Output - Array of element indeces that add up to target int (smaller index first), must be different indexed elements
        Constraints - Array is never empty 

        Plan
        Brute Force:
        Nested loop to check potential elements that can add up with current element to get target int 
        Append indices to result array 

        Hashmap approach:
        Initialize empty hashmap 
        Loop through array and subtract current element from target 
        check if resulting int is in hasmap, if not add current element and index to hashmap 
        if int already in hasmap, return index array of current element and resulting int 
        '''

        value_map = {}

        for num in range(len(nums)):
            k = target - nums[num]

            if k in value_map:
                return [value_map[k], num]

            value_map[nums[num]] = num

'''
Analysis:
Avg time: O(n) + O(1) = O(n) [Brute force-> O(n^2)]
Space: O(n)
'''