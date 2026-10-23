class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        left=""
        right=""
        clean = ""
        for ch in s:
            if ch.isalnum():
                clean += ch
        if len(clean)<2:
            return True
        left=clean[:len(clean)//2]
        right=clean[-(len(clean)//2):]
        if left[::-1]==right:
            return True
        else:
            return False
        
