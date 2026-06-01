class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for word in strs:
            key = "".join(sorted(word))
            hm[key] = hm.get(key, []) + [word]
        return list(hm.values())