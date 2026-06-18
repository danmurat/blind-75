class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                # check for pop
                if stack:
                    top: int = len(stack) - 1
                    if (c == ')' and stack[top] != '(') or (c == '}' and stack[top] != '{') or (c == ']' and stack[top] != '['):
                        return False
                    else:
                        stack.pop()
                else:
                    # if there's nothing in the stack, it can't be valid
                    return False
        
        # if empty, then it was valid!
        return not stack