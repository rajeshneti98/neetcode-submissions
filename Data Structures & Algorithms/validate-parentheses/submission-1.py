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
                if not (( top == '(' and ch == ')') or ( top == '{' and ch == '}') or ( top == '[' and ch == ']')):
                    return False
        return len(stack) == 0