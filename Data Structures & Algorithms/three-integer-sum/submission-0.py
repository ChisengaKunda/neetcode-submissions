class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)

        for i in range(len(nums)-1, 1, -1):
            left, right = 0, i - 1

            while left < right:
                n = nums[left] + nums[right]
                
                if n == -nums[i]:
                    res.add((nums[left], nums[right], nums[i]))
                    left += 1
                    right -= 1 

                elif n < -nums[i]:
                    left += 1
                
                else:
                    right -= 1


        return [list(triplet) for triplet in res]

