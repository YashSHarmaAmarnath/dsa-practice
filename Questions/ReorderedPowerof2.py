class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def permute(num,first=True):
            if len(num)<=1:return [num]
            res = []
            for i in range(len(num)):
                # if i == 0 and num[i] == '0':
                #     continue
                if first and num[i] == '0':
                    continue
                for p in permute(num[:i]+num[i+1:],False):
                    res.append(num[i]+p) 
            return res
        def pov2check(num):
            return num>0 and (num & (num-1)) == 0
        n = str(n)
        permutations = [int(n) for n in permute(n)]
        for n in permutations:
            if pov2check(n):
                return True
        return False
