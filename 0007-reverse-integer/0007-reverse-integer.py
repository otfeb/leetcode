class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        result = 0

        if x > 0:
            sign = 1
        else:
            x *= -1
            sign = 0

        num = [int(a) for a in str(x)]

        while True:
            if num[-1] == 0:
                num.pop()
            else:
                break

        for i in range(len(num)):
            result += num[i] * (10**i)

        if sign == 0:
            result *= -1

        if -2**31 <= result <= 2**31 - 1:
            return result
        else:
            return 0