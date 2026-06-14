class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        The main idea is to represent something in a key that 
        all other strings can instantly compare to. Rather than
        having each key as a single char for a whole string. How
        would another string compare against all of that? They can't.
        You have to go one by one, and it requires you to compare
        all other strings against one in O(n^2).

        The better solution finds a way to represent an anagram
        such that all other anagrams would be equal to it. E.g,
        if you encode a string into a 26 letter array with frequency
        counts (so [a, b, c], but they have ints, [3, 0, 1]), then
        all anagrams would be equal to it.

        This means that if you put this as a key, other strings can
        instantly compare (after they've built their array). if
        equal, append to value's list. If not, create new key and list.
        This is done in one pass O n. The building the array is
        O m, hence we get O(n * m).
        """
        group_hash: dict[tuple[int], list[str]] = {}

        for s in strs:
            alph_count: list[int] = [0] * 26
            group_anag: list[str] = []
            group_anag.append(s)
            for c in s:
                alph_count[ord(c) - ord('a')] += 1

            alph_count_tup: tuple[int] = tuple[int](alph_count)
            if alph_count_tup in group_hash:
                group_hash[alph_count_tup].append(s)
            else:
                group_hash[alph_count_tup] = group_anag

        return_list: list[list[str]] = []
        for k in group_hash.keys():
            return_list.append(group_hash[k])


        return return_list




