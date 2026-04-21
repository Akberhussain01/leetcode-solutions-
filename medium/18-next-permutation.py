class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        
        # 1. find decreasing index
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            # 2. find just greater element
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            # 3. swap
            nums[i], nums[j] = nums[j], nums[i]
        
        # 4. reverse right part
        left = i + 1
        right = n - 1
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
