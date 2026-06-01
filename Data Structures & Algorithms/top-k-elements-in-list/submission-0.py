class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        for i in nums:
            hm[i] = hm.get(i,0)+1
        sorted_keys = sorted(hm, key=hm.get, reverse=True)
        ans = sorted_keys[:k]
        return ans
        