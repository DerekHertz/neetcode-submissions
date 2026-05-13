class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for i in s:
            if i in bracket_map.values():
                stack.append(i)
            if i in bracket_map.keys():
                if len(stack) == 0:
                    return False
                elif stack[len(stack) - 1] != bracket_map[i]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
