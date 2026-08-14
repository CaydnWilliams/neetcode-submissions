class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_map = set()
        for i in range(len(nums)) :
            if nums[i] in dup_map :
                return True
                break
            else :
                dup_map.add(nums[i])
        return False