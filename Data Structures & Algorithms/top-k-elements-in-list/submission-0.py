class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Understand
        Input: array, int k 
        Output: Top k frequent elements
        Constraints: nums is never empty, nums is always int 

        Plan
        Create frequency map for array
        Heapify (max heap) list of tuples containing freq and value in that order
        Loop through heap k times returning other value in tuple 
        '''
        

        freq = {}

        for i in nums:
            if i not in freq:
                freq[i] = 1

            else:
                freq[i] += 1

        heap = []
        for key, val in freq.items():
            heap.append((-val, key))

        heapq.heapify(heap)

        res = []
        for i in range(k):
            a = heapq.heappop(heap)
            res.append(a[1])

        return res

