class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if both strings are the same length, if diff --> false
        if len(s) != len(t):
            return False

        s_dict = dict()
        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1
        
        t_dict = dict()
        for letter in t:
            if letter in t_dict:
                t_dict[letter] += 1
            else:
                t_dict[letter] = 1

        # Check if both dictionaries are the same
        if s_dict == t_dict:
            return True
        
        return False