class Solution:
    def maximum69Number (self, num: int) -> int:
        nuList = list(str(num))
        for i in range(len(nuList)):
            if nuList[i] == '6':
                nuList[i] = '9'
                break
        return int("".join(nuList))

