class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force till i can figure out how to solve in O(n)
        days_till_warmer: list[int] = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    days_till_warmer[i] = j - i
                    break # we only need the first

        
        return days_till_warmer