class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            elif not stack:
                return False
            else:
                top = stack.pop()
                if (top == '(' and ch == ')') or (top == '{' and ch == '}') or (top == '[' and ch == ']'):
                    continue
                else:
                    return False
        return len(stack) == 0
        