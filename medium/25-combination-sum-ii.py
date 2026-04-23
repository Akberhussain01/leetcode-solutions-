class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        
        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                
                # skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                
                # i + 1 क्योंकि reuse allowed नहीं
                backtrack(i + 1, path, remaining - candidates[i])
                
                path.pop()
        
        backtrack(0, [], target)
        return result
