import math

class Solution:
    def isHappy(self, n: int) -> bool:
        def sqr(num):
            sum = 0
            while num > 0:
                r = num % 10
                sum += r**2
                num = num // 10
            return sum

        # Iterate for a fixed number of steps to check for happiness
        for i in range(70):
            n = sqr(n)
            if n == 1:
                return True

        # If the loop completes without finding 1, return False
        return False



if __name__ == '__main__':
    print(Solution().isHappy(2))
