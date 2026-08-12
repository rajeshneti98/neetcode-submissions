class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = {}
        for ch in s:
            mp[ch] = mp.get(ch, 0) + 1
        for ch in t:
            if ch not in mp or mp[ch] <=0:
                return False
            mp[ch] -=1
        for key, val in mp.items():
            if val != 0:
                return False
        return True
        
        