class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31
        INT_MAX =  2**31

        x_str = str(x)
        rev_x_str = x_str[::-1]
        if rev_x_str.endswith("-"):
            rev_x_str = "-" + rev_x_str[:-1]
        res = int(rev_x_str)
        if res not in range( INT_MIN, INT_MAX):
            return 0
        return res
        