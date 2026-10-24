class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        best=0
        l=0
        for right in range(len(s)):
            x=s[right]
            if x not in seen:
                seen.add(x)
            else:
                best=max(best,len(seen))
                while x in seen:
                    seen.remove(s[l])
                    l+=1
                seen.add(x)
            best = max(best, len(seen))
        return best