class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Understand
        Input: Array
        Output: Length of logest consecutive sequence of elements that can be from array
        Constraints: Array can be empty and nums can be positive or negative int
        
        Plan
        Sort array, use 2 pointers to track the longest consecutive array while ignoring immediate duplicates byt adding to  a set 
        Clear set everytime sequence is disturhbed but keep length 
        return maximum length  
        '''
        if not nums:
            return 0
        nums.sort()

        curr_len = 1
        max_len = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                curr_len += 1

            if nums[i] == nums[i-1]:
                continue 
            
            if nums[i] - nums[i - 1] != 1:
                curr_len = 1
            
            max_len = max(max_len, curr_len)
        return max_len

'''
Avg time: O(nlogn) + O(n) = O(nlogn)
Space = O(n)
'''
        