"""
Problem: Longest Substring Without Repeating Characters
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty: Medium

Approach:
- Use sliding window with two pointers
- Maintain a set to track unique characters
- Shrink window when duplicate found

Time: O(n)
Space: O(n)
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length
