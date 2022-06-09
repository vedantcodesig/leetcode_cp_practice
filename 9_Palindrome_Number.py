class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x=str(x)
        rstr=str_x[::-1]
        if str_x==rstr:
            return True
        else:
            return False
        