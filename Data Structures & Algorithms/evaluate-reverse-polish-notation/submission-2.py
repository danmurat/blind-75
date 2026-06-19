class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        """
        1,1,1,+ breaks the test case; so there will only ever really be at most 2
        digits to work with.
        Nvm i was wrong

        Problem: we're not handling negative numbers!
        """

        stack: list[int] = []
        
        # O(n)
        for c in tokens:
            end: int = len(stack) - 1
            if c.isdigit():
                stack.append(int(c))
            elif len(c) > 1 and c[0] == "-" and c[1:].isdigit():
                stack.append(-int(c[1:]))
            elif c == "+":
                stack[end - 1] = stack[end - 1] + stack[end]
                stack.pop()
            elif c == "-":
                stack[end - 1] = stack[end - 1] - stack[end]
                stack.pop()
            elif c == "*":
                stack[end - 1] = stack[end - 1] * stack[end]
                stack.pop()                               
            elif c == "/":
                flt: float = stack[end - 1] / stack[end]
                stack[end - 1] = math.floor(flt) if flt > 0 else math.ceil(flt) # 'division always truncates towards zero'
                stack.pop()
            
            print(f"stack={stack}")

        return stack.pop()
