class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Understand
        Input: Array of strings 
        Output: Array of strings that are anagrams grouped together
        Constraints: Array will have at least 1 string, the string can be empty or at max 100 characters long 

        Plan
        if len(array) < 2:
            return array[0]
        Initialize empty hashmap
        loop through given array, if sorted version of a string is in map add unsorted version to value list for that string assortment
        return values in list form 
        '''


            
        group_map = {}

        for i in strs:
            k = ''.join(sorted(i))

            if k not in group_map:
                group_map[k] = [i]
            
            else:
                group_map[k] += [i]
        
        return list(group_map.values())

'''
Anlysis
avg time: O(n * m) 
space: O(n)
'''