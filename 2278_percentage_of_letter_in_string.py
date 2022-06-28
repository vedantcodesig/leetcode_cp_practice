class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        lc=0
        total=len(s)
        for char in s:
            if char==letter:
                lc+=1
        return int((lc/total)*100)