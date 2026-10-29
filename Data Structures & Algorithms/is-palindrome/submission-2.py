class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Understand
        Input: string
        Output: bool, whether the given string is a palindrome 
        Constraints: string is never empty, s is only printable ASCII characters

        Plan: 
        Use 2 pointers to check if characters from the end and front are the same while checking if they are alphanumeric
        '''

        left = 0 
        right = len(s) - 1

        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False 
                
                left += 1
                right -= 1
            elif not s[left].isalnum():
                left += 1
            
            elif not s[right].isalnum():
                right -= 1
        return True
            

'''
Analysis:
Avg time: O(n) 
Space: O(1)
'''