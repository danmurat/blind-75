class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe_dict: dict[int, int] = {}
        for i in nums:
            if i not in dupe_dict:
                dupe_dict[i] = 0 # give 0, doesn't really matter
            else:
                # if we already find i in key, it's a dupe!
                return True

        # nothing would be dupe if we get here   
        return False