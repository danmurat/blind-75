class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        act, pots, tops, ...
        first need to determine what is an anagram of what
        then group them

        for each strs
        create str dict (with frequency counts for letters)
        check all other strs to see if they match the first (subtracting frequencies of o.g)
        those that match are appended to their own list
        then these grouped lists are returned.

        But this can be super slow.. we do O(n^2) check against all other strs, but it's
        actually O(n^3) because each letter has to be looped through too!

        Can be reduced to O(n^2) i think, if part 1 is done in one pass O(n). Instead of each str
        checking all other strs, once a str is grouped, we don't check any in that group anymore.
        Only ones that are not in any group. Same applies to any new groups. So in the end,
        the first pass does O(n) checks (doesn't re-check any).
        - This can only be done if we use a hash to check a group already. So moving i-th in list,
        we know to move on if list[i] is in dict, which is O(1) check.
        """

        grouped_dict: dict[str, None] = {}
        final_list: List[List[str]] = []

        for i in range(len(strs)):
            if strs[i] not in grouped_dict:
                str_dict: dict[str, int] = {}
                group_list: List[str] = []
                group_list.append(strs[i])
                # build a dict for the string
                for c in strs[i]:
                    if c not in str_dict:
                        str_dict[c] = 1
                    else:
                        str_dict[c] += 1

                for j in range(i + 1, len(strs)):
                    new_dict = str_dict.copy() # we need an original to maintain the same counts (since we decrement)
                    is_anag = True
                    for c in strs[j]:
                        if c in new_dict:
                            new_dict[c] -= 1
                        else:
                            is_anag = False
                            break
                    # another falsehood check
                    if is_anag: 
                        for k in new_dict.keys():
                            if new_dict[k] != 0:
                                is_anag = False
                    if is_anag:
                        # add to list and grouped
                        group_list.append(strs[j])
                        grouped_dict[strs[j]] = None

                final_list.append(group_list)
        
        return final_list



