class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Sort list (otherwise pointers are kind of useless)
        p1, p2, p3. p1/p3 at start/end.
        p2 i think can go anywhere in the middle? But probs
        place it directly after p1 (p1+1). Then we use
        the same logic as 2sum, move p's depending on sum
        result.

        First attempt p1/p3 move, but if p2 is directly next
        (stopping them from moving), move p2 instead.

        Eventually they'll all be next to each other and should
        hopefully have covered all possibilites.

        Struggling with 2 things. 1, my while loop doesn't terminate
        on some tests (need to actually look at closely). 2 is test case
        19, and making sure i don't include dupelicate triplets.
        The best thing I can think of is straight up removing dupelicates
        in the num list after sorting. If one of my pointers move, and it still
        sums to 0 - even if the numbers haven't changed - it will add it, being
        a dupelicate. If the same number doesn't exist, we don't get this problem.

        Nvm, removing dupes stops us from finding valid solutions...
        Will come back to it tomorrow.
        Changing strat to index i + p1,p2 (keeping it at 2 p) + keeping our dupe
        check.
        """
        nums.sort()
        sum_list: list[list[int]] = []
        nums_len = len(nums)
        print(nums)

        for i in range(nums_len):
            p1: int = i + 1
            p2: int = nums_len - 1
            while p1 < p2:
                sum3: int = nums[i] + nums[p1] + nums[p2]
                if sum3 < 0:
                    p1 += 1
                elif sum3 > 0:
                    p2 -= 1
                else:
                    valid_triplet: list[int] = [nums[i], nums[p1], nums[p2]]
                    valid_triplet.sort()
                    if not self._is_dupe(valid_triplet, sum_list):
                        sum_list.append(valid_triplet)
                    p1 += 1 # moving either one in this case shouldn't matter
        
        return sum_list
    
    def _is_dupe(self, valid: list[int], sum_list: list[list[int]]) -> bool:
        for sl in sum_list:
            if valid[0] == sl[0] and valid[1] == sl[1] and valid[2] == sl[2]:
                return True

        return False


        """
        while p2 != p1 and p2 != p3: # this means p2 is directly middle, and they can no longer move
            print(f"{p1} | {p2} | {p3} | {p4}")
            sum3_1 = nums[p1] + nums[p2] + nums[p4]
            sum3_2 = nums[p1] + nums[p3] + nums[p4]
            ovrl_sum = sum3_1 + sum3_2 # help us decide which pointer to move
            if sum3 < 0:
                if p2 == p1+1 and p2+1 != p2_stack[0]:
                    p2_stack[0] = p2 # pop and push (just by replacing)
                    p2 += 1
                else:
                    p1 += 1
            elif sum3 > 0:
                if p2 == p3-1 and p2-1 != p2_stack[0]:
                    p2_stack[0] = p2
                    p2 -= 1
                else:
                    p3 -= 1
            else:
                valid_triplet: list[int] = [nums[p1], nums[p2], nums[p3]]
                valid_triplet.sort()
                if not self._is_dupe(valid_triplet, sum_list):
                    sum_list.append([nums[p1], nums[p2], nums[p3]])
                if p2 == p1+1: # we want to be moving the ends
                    p3 -= 1
                else:
                    p1 += 1

        return sum_list

        """

        """
        Primarily stuck on the dupelicate handling. Our 3 pointers end up traversing
        the same triplets again (on different indexes), which is not allowed. But how
        do I stop this? Remember, the triplets doesn't even have to be the same order,
        just that they don't contain the same elements. Using a hash would increase
        space above O(1) recommendation (which was the beauty of pointers), but how
        would we deal with DIFFERENT dupelicates? I would have to loop through
        different hashes to check. But the elements can have dupes within (like 2 one's),
        which a hash can't hold.

        Otherwise can sort the triplet's into a check list, go though and compare by
        index whether the incoming triplet is equal to any triplets in the list
        (check [0][1][2]).
        Triplets can be in any order, so this wouldn't matter (and potentially a hint
        for doing exactly this?)
        I think this makes it O(n * m * 3*logn)
        --
        Above working, but turns out my 3 pointers don't have enough coverage. Having
        an extra mid pointer, but by the end should be enough. Though the logic
        will get a bit more dense, since I'd have to decide what to move.

        """









