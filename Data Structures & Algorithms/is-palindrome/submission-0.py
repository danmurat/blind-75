class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        two pointer, start and end.
        Palindrome is same when read backwards, so start and
        end must be identical. Move to center, and if at any
        point they're not equal, return false.
        """
        s = s.lower()
        alphnum_str: list[str] = [c for c in s if c.isalnum()]
        str_length = len(alphnum_str)
        ps: int = 0
        pe: int = str_length - 1
        while ps < pe:
            if alphnum_str[ps] != alphnum_str[pe]:
                return False
            else:
                ps += 1
                pe -= 1

        return True
