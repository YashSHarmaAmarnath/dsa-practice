class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = dividend/divisor
        if res>2**31-1:
            return 2**31-1
        if res<-2**31:
            return -2**31
        if res<0:
            return math.ceil(res)
        else:
            return math.floor(res)
