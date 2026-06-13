class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # anagrams always contain the same characters
        # basically we need to check if a character is not
        # contained in the other string

        # create a hash
        # add vals from s to hash (first loop)
        # do another loop for t to check if element not a key in hash

        # their lengths must be the same to be an anagram!
        if len(s) != len(t):
            return False

        hashmap1 = {}
        hashmap2 = {}

        for i in s:
            if i not in hashmap1:
                hashmap1[i] = 1
            else:
                hashmap1[i] += 1 # increase the count

        
        for i in t:
            if i not in hashmap1:
                return False # t contains char not in s
            else:
                # add vals to hashmap2 so we can compare counts
                if i not in hashmap2:
                    hashmap2[i] = 1
                else:
                    hashmap2[i] += 1
                    if hashmap2[i] > hashmap1[i]:
                        return False
        
        return True