class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = []
        val = (-10**9)-1

        for i in range(len(nums)-1, -1, -1):
            if nums[i] < val:
                return True
            while stack and stack[-1] < nums[i]:
                val = stack.pop()
            stack.append(nums[i])

        return False