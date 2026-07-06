class Solution:
    def missingNumber(self, nums):
        expected = 0
        actual = 0

        for i in range(len(nums) + 1):
            expected += i

        for num in nums:
            actual += num

        return expected - actual  