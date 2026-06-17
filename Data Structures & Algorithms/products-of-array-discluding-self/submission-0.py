class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        o[i] = all of nums multiplied, apart from nums[i]

        def going to have multiple O(n) passes.
        the brute force here is double looping i,j; where
        you just do all j * j's and place it into o[i] for
        each i.

        But in linear time?

        Ends up being a clever trick using products of prefixes and suffixes.
        When you build a prefix, each index includes the product of all
        elements to it's left. Suffix is all elements to its right (from right-left).
        So each has all other products (for each side) but not the other. Multiplying
        these is the final bridge, and each index will have the product of all others.
        Nicely done in O(n).
        """

        nums_len = len(nums)
        prefix: list[int] = [0] * nums_len
        suffix: list[int] = [0] * nums_len
        p_prod: int = 0
        s_prod: int = 0
        for i in range(nums_len):
            p = i
            s = nums_len - i - 1
            if p == 0 and s == nums_len -1:
                prefix[p] = 1
                p_prod = nums[p]
                suffix[s] = 1
                s_prod = nums[s]
            else:
                prefix[p] = p_prod
                p_prod *= nums[p]
                suffix[s] = s_prod
                s_prod *= nums[s]
        
        return [prefix[i] * suffix[i] for i in range(nums_len)]




        