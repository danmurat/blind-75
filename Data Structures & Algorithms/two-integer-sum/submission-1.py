class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # first thought
        # just double loop and compare each addition to target

        # can this be done in O(n)??
        # I can't really think of a way to do this linearly.
        # By it's nature, all numbers have to be checked against all others.


        # double loop implementation. Time: O(n^2), Space: O(1)

        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [min(i, j), max(i, j)]
