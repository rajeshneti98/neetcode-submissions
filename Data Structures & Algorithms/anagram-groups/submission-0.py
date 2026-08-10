class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            counter = Counter(s)
            st = ''
            for key in sorted(counter.keys()):
                st+=key
                st+= str(counter[key])+' '
            if st not in map:
                map[st] = [s]
            else:
                map[st].append(s)
        return list(map.values())