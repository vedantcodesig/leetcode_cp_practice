class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''.join(char for char in s if char.isalnum())
        new_string1=new_string.lower()
        if new_string1==new_string1[::-1]:
            return True
        else:
            return False