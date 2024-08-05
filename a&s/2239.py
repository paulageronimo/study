class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        cl_zer = nums[0]

        for num in nums:
            if abs(num) < abs(cl_zer):
                cl_zer = num
            elif abs(num) == abs(cl_zer) and num > cl_zer:
                cl_zer = num
        
        return cl_zer
      
# Runtime 
# 113 ms | Beats 91.58% | O(n)

# Memory
# 16.75 mb | Beats 59.54% | O(1)