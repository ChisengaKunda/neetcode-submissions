class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Understand 
        Input: String
        Output: Length of longest consecutive substring with no repeating characters
        Constriants: String may be empty
        Plan:
        Loop through string while adding unique characters to set, if char already in set, update max_len, clear set and move left pointer by 1 and right pointer to left pointer pos
        '''

        if len(s) == 1:
            return 1

        seen = set()
        l, r = 0, 0
        max_len = 0
        curr_len = 0

        while r < len(s):
            while s[r] in seen:
                max_len = max(max_len, len(seen))
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            curr_len = len(seen)
            r += 1
        return max(max_len, curr_len)


        