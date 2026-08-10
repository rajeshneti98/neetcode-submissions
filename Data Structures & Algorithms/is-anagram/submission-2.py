class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            d1[s[i]]+=1
            d2[t[i]]+=1
        return d1 == d2