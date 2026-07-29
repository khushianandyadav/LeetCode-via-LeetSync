class Solution(object):
    def lowerBound(self, nums, target):
        n = len(nums)
        lb = n
        low = 0
        high = n-1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid-1
            else:
                low = mid+1
        return lb


    def upperBound(self, nums, target):
        n = len(nums)
        ub = n
        low = 0
        high = n-1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] > target:
                ub = mid
                high = mid-1
            else:
                low = mid+1
        return ub



    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        lb = self.lowerBound(nums, target)
        if lb == n or nums[lb] != target:
            return [-1, -1]
            

        ub = self.upperBound(nums, target)
        return [lb, ub-1]
        
        