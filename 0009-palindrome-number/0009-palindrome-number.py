import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(math.ceil(len(x)/2)):
            for j in range((len(x)-1)-i, (len(x)//2)-1, -1):
                if x[i] != x[j]:
                    return False
                else:
                    break
        return True