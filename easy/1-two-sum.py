"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy

Approach:
- Use HashMap to store visited numbers
- Check complement in O(1)

Time: O(n)
Space: O(n)
"""

class Solution:
    def twoSum(self, nums, target):
        num_map = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in num_map:
                return [num_map[complement], i]
            
            num_map[nums[i]] = i
