class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            st = str(i)
            if len(st)%2 == 0:
                count = count + 1
        return count