class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {
            ')':'(', 
            '}': '{',
            "]": '['
        }

        my_list = list()
        for char in s:
            if char in my_dict.keys():
                if my_list and my_list[-1] == my_dict[char]:
                    my_list.pop()
                else: return False
            else:
                my_list.append(char)
        return len(my_list) == 0

                
        