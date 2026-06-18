class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_hash: dict[tuple, list] = {}

        for s in strs:
            alph_freq: list = [0] * 26
            for c in s:
                alph_freq[ord(c) - ord('a')] += 1
            
            # convert to tup and check against hash
            alph_freq_tup: tuple = tuple(alph_freq)
            if alph_freq_tup not in group_hash:
                group_hash[alph_freq_tup] = [s]
            else:
                group_hash[alph_freq_tup].append(s)

        
        return [group_hash[k] for k in group_hash.keys()]