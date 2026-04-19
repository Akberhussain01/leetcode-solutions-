class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)
        
        # 1. skip spaces
        while i < n and s[i] == ' ':
            i += 1
        
        # 2. check sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # 3. convert digits
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit
            i += 1
        
        result *= sign
        
        # 4. handle overflow
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result
