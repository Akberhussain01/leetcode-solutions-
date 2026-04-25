class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        result = []
        used = [False] * len(nums)
        
        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                
                if used[i]:
                    continue
                
                # skip duplicates
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                path.append(nums[i])
                used[i] = True
                
                backtrack(path)
                
                path.pop()
                used[i] = False
        
        backtrack([])
        return result
