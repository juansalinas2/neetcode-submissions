class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_counter = 0

        for num in nums:
            if num == 1:
                counter += 1
            else: counter = 0

            if counter > max_counter:
                max_counter = counter
        return max_counter