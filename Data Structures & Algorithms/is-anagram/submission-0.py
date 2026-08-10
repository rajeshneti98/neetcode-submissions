class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for ch in s:
            if ch in map:
                map[ch]+=1
            else:
                map[ch]=1
        for ch in t:
            if ch in map:
                map[ch]-=1
            else:
                map[ch]=-1
        for num in map.values():
            if num!=0:
                return False
        return True        