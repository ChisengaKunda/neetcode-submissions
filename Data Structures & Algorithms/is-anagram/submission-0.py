class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Understand:
        Input - 2 strings 
        Output - bool, whether they have exaclty the same characters
        Constraints - Both strings in lower case, strings cannot be empty, 

        Plan:
        if different lengths, immediate false 
            sort both strings, compare - route 1 
            Route 2:
            Frequency map for first string
            Traverse 2nd string sutracting 1 from count at every occurence of the same char
            If char is not in frequency map, return False 
            if count is -1, return False

        Implementation:
        '''
        # if len(s) != len(t):
        #     return False 
        # s = sorted(s)
        # t = sorted(t)

        # return s == t

        if len(s) != len(t):
            return False 

        freq = {}

        for char in s:
            if char in freq:
                freq[char] += 1
            
            else:
                freq[char] = 1
        
        for char in t:
            if char not in freq:
                return False 
            
            freq[char] -= 1
            if freq[char] < 0:
                return False
        return True 


'''
Analysis: 
average time:
O(n + m)
space = O(n)
'''

        