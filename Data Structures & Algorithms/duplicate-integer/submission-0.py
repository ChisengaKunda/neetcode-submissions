class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        1. Understand:
        Input: Array - nums 
        Output: bool - whether arr has duplicates
        Constraints: Array can be empty or 10^5, Array can contain large or small int. 

        2. Plan:
        Data Structure - Set  
        Loop through array, add element, if element already in set, return True, Else False 

        """
        #Implementation: 
        seen = set()

        for num in nums:
            if num in seen:
                return True 
            
            seen.add(num)
        return False 


"""
Analysis:
Time Complexity (average time) - loop O(n), set addition O(1), Total -- O(n)
Space Complexity - Set O(n)

"""

        