class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [-i for i in nums]
        heapq.heapify(minHeap)

        ans = None
        while k > 0:
            ans = -heapq.heappop(minHeap)
            k -= 1

        return ans 
