class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Understand 
        Input:Array, target int
        Output: 1 indexed pair of indexes that add up to target int
        Constraints: There is always an answer, array elements can be positive or negative
        '''   
        i = 0
        j = len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1

            elif numbers[i] + numbers[j] < target:
                i += 1
            
            else:
                return [i+1, j+1]

'''
Avg time: O(n)
Space: O(n) because of the array created at the end 
'''