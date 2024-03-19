class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            if i % 3==0 and i % 5 == 0:
                i = "FizzBuzz"
                res.append(i)
            elif i % 5 == 0:
                i = "Buzz"
                res.append(i)
            elif i % 3 == 0:
                i = "Fizz"
                res.append(i)
            else:
                res.append(str(i))
        return res