class Solution:
    def divide(self, dividend, divisor):
        # handle overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # determine sign
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        result = 0
        
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            
            # double divisor until too large
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            dividend -= temp
            result += multiple
        
        return sign * result
