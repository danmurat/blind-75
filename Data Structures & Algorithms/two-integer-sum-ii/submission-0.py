class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        O(1) spacError, e, so we know we cannot use any extra lists or
        hashes. Two pointer. But how?
        
        p1 = start, p2 = end
        increment p1 if sum is less than target
        dec p2 if sum is more
        if equal we return indexes.

        Think this has enough coverage for all possible sums? (since list is sorted).
        """

        num_len: int = len(numbers)
        p1: int = 0
        p2: int = num_len - 1
        while p1 < p2:
            two_sum: int = numbers[p1] + numbers[p2]
            if two_sum < target:
                p1 += 1
            elif two_sum > target:
                p2 -= 1
            else:
                return [p1+1, p2+1] # 1-indexed


        
        raise ValueError("You found no solution. There should be a solution")
