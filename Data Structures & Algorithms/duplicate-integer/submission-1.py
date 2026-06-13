class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # n^2 solution:
        # double loop. First contains the checker
        # second loop compares other elements to checker
        # false if found
        # if double loop ends, then no dupes

        """
        for i in range(len(nums)):
            checker: int = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == checker:
                    return True
        
        return False
        """

        # what about O(n) ??

        # what if we create a histogram like count for each index?
        # if some count >= 2, then false?
        # so as we iterate linearly, we add some value to a newly created list
        # value 1 goes to list 1, if list1 >= 2 then false
        # we do this check every time

        hashmap = {}

        for i in nums:
            # first check if key exists
            if i not in hashmap:
                hashmap[i] = 1 # add a count to this value
            else:
                return True # value already exists, so it's a dupe

        return False
