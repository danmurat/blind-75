class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Intermediate values don't matter. We only care about biggest, next biggest, etc.
        The thing I didn't understand was tracking the indexes themselves, and arranging
        them by the values at those index. Because we care about DISTANCE mainly, but the
        arrangement, the biggest/nextbiggest, that's the values AT those indexes.

        If you build a stack starting from the end of temps, you make sure the stack
        is in decreasing order (monotonic), so whenever new values come in, you 'pop'
        those that are smaller than the current value, until there isn't any smaller ones.
        Because you're saving indexes however, once you stop 'popping', you know the distance
        to the next biggest!
        """
        mono_stack: list[int] = []
        days_till_warmer: list[int] = []
        temp_len: int = len(temperatures)
        
        for i in range(temp_len -1, -1, -1):
            if not mono_stack:
                mono_stack.append(i)
                days_till_warmer.append(0)
            else:
                while mono_stack and (temperatures[i] >= temperatures[mono_stack[len(mono_stack) - 1]]):
                    mono_stack.pop()

                mono_stack.append(i)
                stack_len = len(mono_stack)
                if stack_len == 1: 
                    days_till_warmer.append(0) # it's the warmest day so far
                else:
                    days_till_warmer.append(mono_stack[stack_len - 2] - mono_stack[stack_len - 1])
                # print(mono_stack)
                # print(days_till_warmer)


        days_till_warmer.reverse()
        return days_till_warmer



