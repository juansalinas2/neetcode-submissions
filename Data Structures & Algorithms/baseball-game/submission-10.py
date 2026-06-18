class Solution:
    def calPoints(self, operations: List[str]) -> int:
        my_list = list()
        for item in operations:
            if item == '+':
                my_list.append(int(my_list[-1])+int(my_list[-2]))
            elif item == 'C':
                my_list.pop() 
            elif item == 'D':
                my_list.append(2*int(my_list[-1]))
            else: # item is an integer
                my_list.append(int(item))

        return sum(my_list)