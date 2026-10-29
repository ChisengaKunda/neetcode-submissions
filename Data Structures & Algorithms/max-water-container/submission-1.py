class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        Understand
        Input: Array of heights 
        Output: Max possible area from given heights and calculated widths 
        Constraints: Array will always have at least 2 elements, height can be 0

        Plan:
        Use 2 pointers from either end of array, keep a running maximum area, use a loop and calculate area at every iteration and comparing calculated area with stored max area
        Move pointer on side of shorter height or either on equal heights
        return max_area
        '''

        
        left, right = 0, len(heights) - 1 

        max_area = 0

        while left < right:
            area = min(heights[left], heights[right])* (right - left)
            max_area = max(area, max_area)

            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return max_area 

'''
Avg time: O(n) 
Space: o(1)
'''