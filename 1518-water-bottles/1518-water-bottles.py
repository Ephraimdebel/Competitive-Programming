class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = 0
        while numBottles >= numExchange:
            res = numBottles // numExchange
            reminder = numBottles % numExchange
            count += numBottles - reminder
            numBottles = res + reminder
        count += numBottles
        return count