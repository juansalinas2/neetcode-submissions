class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = dict()
        for  char in s:
            dict_s[char] = dict_s.get(char,0)+1  
        
        for char in t:
            dict_s[char] = dict_s.get(char,0)-1
            if dict_s[char] < 0:
                return False
        for char in dict_s.keys():
            if dict_s[char] > 0:
                return False
        return True