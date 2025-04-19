class Solution:
    def missingNumber(self, nums) -> int:
        total = 0
        for i in range(len(nums)+1):
            total += i
        return total - sum(nums)

# -------------------------------

# class Solution:
#     def missingNumber(self, nums) -> int:
#         my_set = set(nums)
#         range_set = set(range(len(nums) + 1))
#         return (range_set - my_set)




# Example Usage

sol = Solution()

# Example 1
nums1 = [3, 0, 1]  # Missing number is 2
print("Missing Number (Example 1):", sol.missingNumber(nums1))

# Example 2
nums2 = [0, 1]  # Missing number is 2
print("Missing Number (Example 2):", sol.missingNumber(nums2))

# Example 3
nums3 = [9,6,4,2,3,5,7,0,1]  # Missing number is 8
print("Missing Number (Example 3):", sol.missingNumber(nums3))

# Example 4
nums4 = [0]  # Missing number is 1
print("Missing Number (Example 4):", sol.missingNumber(nums4))

