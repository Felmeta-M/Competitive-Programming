class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < 3:
            return nums[-1]
        myset = set(nums)
        return list(myset)[-3]
