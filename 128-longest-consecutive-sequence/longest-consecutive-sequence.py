class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        last_smaller = float("-inf")
        longest = 0
        for i in range(0, n):
            num = nums[i]
            if num-1 == last_smaller:
                count += 1
                last_smaller = num
            elif num != last_smaller:
                count = 1
                last_smaller = num
            longest = max(longest, count)
        return longest
        