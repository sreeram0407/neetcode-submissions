class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = {}
        hm2 = {}
        for i in range(len(s)):
            hm1[s[i]] = hm1.get(s[i],0)+1
        for i in range(len(t)):
            hm2[t[i]] = hm2.get(t[i],0)+1
        if hm1 == hm2:
            return True
        else:
            return False
            
        