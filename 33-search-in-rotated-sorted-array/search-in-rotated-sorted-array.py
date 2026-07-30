class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        for i in range(0, n):
            if nums[i] == target:
                return i
        return -1
        