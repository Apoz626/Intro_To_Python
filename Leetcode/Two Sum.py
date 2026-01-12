class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i and nums[i] + nums[j] == target:
                    return 'Match found at indexes: ' + str([i,j]) + ' / Correlating numbers are: ' + str([nums[i], nums[j]])
        return 'No matches found'

s = Solution()
result = s.twoSum([3, 3, 3, 6], 9)

print(result)
