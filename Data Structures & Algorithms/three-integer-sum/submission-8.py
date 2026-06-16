class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        sum_list: list[list[int]] = []
        nums_len = len(nums)
        print(nums)
        i_stack: list = [None]

        for i in range(nums_len):
            p1: int = i + 1
            p2: int = nums_len - 1
            #print(f"i={i} | p1={p1} | p2={p2}")
            p1_stack: list = [None]
            p2_stack: list = [None]
            if nums[i] != i_stack[0]: # glide over dupes
                i_stack[0] = nums[i]
                #counter: int = 0 # use for debugging
                while p1 < p2:
                    p1_stack[0] = nums[p1] # p1 < p2, so it's safe to do this
                    p2_stack[0] = nums[p2]
                    sum3: int = nums[i] + nums[p1] + nums[p2]
                    #print(f"{i} | {p1} | {p2}")
                    if sum3 < 0:
                        while nums[p1] == p1_stack[0] and p1 < p2: # also glide
                            p1 += 1
                        p1_stack[0] = nums[p1]
                    elif sum3 > 0:
                        while nums[p2] == p2_stack[0] and p1 < p2:
                            p2 -= 1
                        p2_stack[0] = nums[p2]
                    else:
                        sum_list.append([nums[i], nums[p1], nums[p2]])
                        while nums[p1] == p1_stack[0] and p1 < p2:
                            p1 += 1 # moving either one in this case shouldn't matter
                        p1_stack[0] = nums[p1]

                    #counter += 1
        
        return sum_list
    
    """
    # there's no need to loop! because the list is already sorted, a dupelicate
    # would mean that the pointer that moved has the same number as previous. The latest
    # in that list is the only relevant one, because if the next pointed num is differnt,
    # it has to be bigger! Because it's sorted! Meaning all previous triplet are irrelevant
    # to check!
    womp i was wrong.
    I think the only way to avoid dupes without adding extra time and space is to glide
    over dupelicate values in the list. if [i] = -4, and the next is -4, this would
    cause dupelicates since the pointers would check sums for all other values AGAIN.
    Gliding over these fixes this, because now you get a new num each time. But only
    for the ith number, not pointers, since pointers gliding could skip out on an important sum.
    (because there's two of them, and only one moves at a time.) Nvm i do need a stack for pointers too.
    """








