class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in hashmap:
                return [hashmap[x],i]
            if num not in hashmap:
                hashmap[num] = i



