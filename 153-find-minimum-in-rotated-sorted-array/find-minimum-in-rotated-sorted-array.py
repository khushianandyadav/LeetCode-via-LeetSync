class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        mini = float("inf")
        for i in range(0, n):
            mini = min(mini, nums[i])
        return mini
        