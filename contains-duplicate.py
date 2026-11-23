class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)
        

nums = [1,1,1,3,3,4,3,2,4,2]

s = Solution()

result = s.containsDuplicate(nums)

print(result)
