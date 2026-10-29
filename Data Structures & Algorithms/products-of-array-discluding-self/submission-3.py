class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Understand 
        Input: Array
        Output: Array of products of every value in array except at index i, for every value in array
        Constraints: The array length is always> 2, product is guaranteed to fit in 32-bit int

        Plan
        
        '''

        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        res = [1]*len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i -1]

            j = len(nums) - 1 - i
            suffix[j] = suffix[j+1] * nums[j + 1]
        
        for i in range(len(nums)):
            res[i] = prefix[i]*suffix[i]

        return res


'''
Analysis:

space:  
'''

            