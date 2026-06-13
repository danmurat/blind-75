class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # first thought
        # just double loop and compare each addition to target

        # can this be done in O(n)??
        # I can't really think of a way to do this linearly.
        # By it's nature, all numbers have to be checked against all others.


        # double loop implementation. Time: O(n^2), Space: O(1)


        """
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [min(i, j), max(i, j)]
        """

        # apparently it's possible to O(n)? with O(n) space
        # how??

        #nums[i] + nums[j] == target
        # re-arranged to:
        #nums[i] - target == -nums[j]
        # this let's us know we need to find the -nums[j] in the list

        #nums[j] - target = -nums[i]
        # and this lets us know which nums[i] to find.

        # this means we can go through the list in 1 go, finding these values!
        # but they still need to be the correct indexes??

        # we can just use 1 of the equations!!
        # ADD LIST TO A HASHMAP!!
        # for each index, find the nums[i] - target = -nums[j]
        # if the nums[j] does not exist in hash, then move on
        # do until loop complete

        hashmap = {}
        ithIndex: int = 0
        jthIndex: int = 0

        for index, value in enumerate(nums):
            # key will be the value, so we can search for it in O(1)
            hashmap[value] = index

        # then do main checking loop
        for i in range(len(nums)):
            jToFind: int = nums[i] - target
            # we need to handle the sign depending on result and target values
            if jToFind < 0:
                jToFind = abs(jToFind)
            else:
                jToFind = -jToFind

            # the finder    
            if jToFind in hashmap:
                ithIndex = i
                jthIndex = hashmap[jToFind]
                # we can't use the same index!
                if ithIndex != jthIndex:
                    return [min(ithIndex, jthIndex), max(ithIndex, jthIndex)]


        
        