class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())

        if len(s) < 1:
            return True
        last = len(s) - 1

        for i, c in enumerate(s):
            if i > last: 
                return True
            if s[i] != s[last]:
                return False
            last -= 1
            if last < 0: 
                return True
        

        