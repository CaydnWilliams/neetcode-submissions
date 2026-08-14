class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoMap = {}

        for i, val in enumerate(nums):
            diff = target - val
            if diff in twoMap :
                return [twoMap[diff], i]
            else :
                twoMap[val] = i
                
        

