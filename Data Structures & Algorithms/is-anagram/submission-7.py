class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # got to be same length
        if len(s) != len(t):
            return False
        
        s_dict: dict[str, int] = {}
        for char_s in s:
            if char_s not in s_dict:
                s_dict[char_s] = 1
            else:
                s_dict[char_s] += 1

        for char_t in t:
            # anagram, so must all must contain same letters!
            if char_t not in s_dict:
                return False
            else:
                s_dict[char_t] -= 1

        # final loop to check frequency of letters are equal (they should all be 0)
        for i in s_dict.keys():
            #print(f"{i}, {s_dict[i]}")
            if s_dict[i] != 0:
                return False

        # O(n) f(n) = 3n
        return True