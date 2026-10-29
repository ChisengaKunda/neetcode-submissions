class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Understand
        Input: string
        Output: bool, whether the given string is a palindrome 
        Constraints: string is never empty, s is only printable ASCII characters

        Plan:
        Create version of string with no spaces and all lower case 
        Use 2 pointers to check if characters from the end and front are the same 
        '''
        string =''

        for i in s:
            if i.isalpha():
                string += i.lower()

            elif i.isnumeric():
                string += i
        print(string)
        left = 0 
        right = len(string) - 1

        while left < right:
            if string[left] != string[right]:
                return False 
            right -= 1
            left += 1
        return True 

