class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # count=0
        # for i in range(len(time)):
        #     for j in range(i+1,len(time)):
        #         if (time[i]+time[j])%60==0:
        #             count+=1
        # return count
        song = [0]*60
        res=0
        for i in time:
            res +=song[-i%60]
            song[i%60]+=1
        return res         
