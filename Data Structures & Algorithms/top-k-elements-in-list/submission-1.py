class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            count[i] = count.get(i,0)+1
        
        
        pairs = []
        for num,freq in count.items():
            pairs.append([freq, num])
        pairs.sort()
        
        ans = []
        for i in range(k):
            ans.append(pairs.pop()[1])
        return ans
