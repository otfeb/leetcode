class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if not stack:
                if s[i] == ')' or s[i] == '}' or s[i] == ']':
                    return False
                
            if s[i] == ')':
                if stack[-1] == '(':
                    stack.pop()
                    continue
            elif s[i] == '}':
                if stack[-1] == '{':
                    stack.pop()
                    continue
            elif s[i] == ']':
                if stack[-1] == '[':
                    stack.pop()
                    continue

            stack.append(s[i])
        if not stack:
            return True
        else:
            return False