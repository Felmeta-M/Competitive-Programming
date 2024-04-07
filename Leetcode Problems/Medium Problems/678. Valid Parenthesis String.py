class Solution:
    def checkValidString(self, s: str) -> bool:
        n: int = len(s)

        memo = {}
        def f(i: int, left: int):

            if (i, left) in memo:
                return memo[(i, left)]

            if i == n:
                if left == 0:
                    return True
                else:
                    return False

            if left < 0:
                memo[(i, left)] = False
            elif s[i] == "(":
                memo[(i, left)] = f(i + 1, left + 1)
            elif s[i] == ")":
                memo[(i, left)] = f(i + 1, left - 1)
            else:
                memo[(i, left)] = f(i + 1, left - 1) | f(i + 1, left + 1) | f(i + 1, left)

            return memo[(i, left)]

        return f(0, 0)