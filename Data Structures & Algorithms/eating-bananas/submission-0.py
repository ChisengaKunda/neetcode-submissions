class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_rate = r

        while l <= r:
            mid = (l + r)//2 
            hours = 0

            for b in piles:
                hours += math.ceil(b/mid)

            if hours <= h:
                min_rate = min(r, mid)
                r = mid - 1 

            else:
                l = mid + 1 

        return min_rate


