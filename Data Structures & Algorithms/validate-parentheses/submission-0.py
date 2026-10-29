class Solution:
    def isValid(self, s: str) -> bool:
        parens = {'(': ')', '[':']', '{': '}'}
        stack = []

        for i in s:
            if i in parens:
                stack.append(i)
            
            else:
                if stack and i == parens[stack[-1]]:
                    stack.pop()

                else:
                    return False 

        return len(stack) == 0

            