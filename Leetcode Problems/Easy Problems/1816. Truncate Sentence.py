class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        splits = s.split()
        res = splits[:k]
        ans = " ".join(res)
        return ans