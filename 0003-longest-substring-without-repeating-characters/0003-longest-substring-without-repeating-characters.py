class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        arr = []
        result = s[0]
        max = -1

        for i in range(1, len(s)):
            if s[i] in result:
                arr.append(result)
                a = result.find(s[i])
                result = result[a+1:]
                result += s[i]
            else:
                result += s[i]
        arr.append(result)

        for val in arr:
            if max < len(val):
                max = len(val)

        return max