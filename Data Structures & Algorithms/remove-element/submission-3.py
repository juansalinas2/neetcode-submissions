class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        len_nums = len(nums)

        # i indexes current save position, j runs through list
        
        for j in range(len_nums):  
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i 


                   
                