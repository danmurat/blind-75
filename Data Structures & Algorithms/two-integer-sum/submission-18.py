class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict: dict[int, int] = {}
        ind_dict: dict[int, int] = {}
        dupe_dict: dict[int, int] = {}
        
        for i in range(len(nums)):
            if nums[i] in num_dict:
                dupe_dict[nums[i]] = i
            else:
                num_dict[nums[i]] = target - nums[i] # value will be int that when added to key == target
                ind_dict[nums[i]] = i # holds index of those nums

        for key in num_dict.keys():
            if num_dict[key] == key:
                dupe_result = self.check_dupe(key, ind_dict, dupe_dict)
                if dupe_result is not None:
                    return dupe_result
            elif num_dict[key] in num_dict:
                return [ind_dict[key], ind_dict[num_dict[key]]]
            
        return [] # this shouldn't happen]

    def check_dupe(self, key: int, ind_dict: dict, dupe_dict: dict) -> List[int] | None:
        if key in dupe_dict:
            return [ind_dict[key], dupe_dict[key]]
