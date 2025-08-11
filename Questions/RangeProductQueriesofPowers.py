class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        n2 = bin(n)[2:][::-1]
        power = []
        for i in range(len(n2)):
            if n2[i] == '1':
                power.append(2**i)
        res = [0]*len(queries)
        for i in range(len(res)):
            pro = 1
            for j in range(queries[i][0],queries[i][1]+1):
                pro*=power[j]
            res[i] = pro % 1000000007
        return res
