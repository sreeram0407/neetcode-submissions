class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm1 = {}
        hm2 = {}
        for i in s:
            hm1[i] = hm1.get(i,0)+1
        for j in t:
            hm2[j] = hm2.get(j,0)+1
        if hm1 == hm2:
            return True
        else:
            return False

