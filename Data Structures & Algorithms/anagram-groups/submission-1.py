class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for a in strs:
            key= ''.join(sorted(a))
            if key in d:
                d[key].append(a)
            else:
                d[key]=[a]
        return list(d.values())