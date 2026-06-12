class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tmp = len(nums)
        ans = [1] * tmp
        left = 1
        for i in range(tmp):
            ans[i] = left
            left *= nums[i]
        right = 1
        for i in range(tmp - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]

        return ans
        