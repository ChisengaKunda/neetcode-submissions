class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for i, j in points:
            distance = (i**2) + (j**2)
            distances.append([distance, i, j])

        heapq.heapify(distances)
        ans = []
        
        for i in range(k):
            d, x, y = heapq.heappop(distances)
            ans.append([x, y])

        return ans
