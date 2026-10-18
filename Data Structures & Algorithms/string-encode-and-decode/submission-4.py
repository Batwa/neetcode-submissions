class Solution:

    def encode(self, strs: List[str]) -> str:
        a=""
        for x in strs:
            a+=x
            a+="я"
        return a
    def decode(self, s: str) -> List[str]:
        lst=[]
        a=""
        for x in s:
            if x!="я":
                a+=x
            else:
                lst.append(a)
                a=""
        return lst
