class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len(people) - 1
        no_bot = 0
        people.sort()
        while l <= r:
            temp =  people[l]+people[r]
            if temp <=limit:
                l+=1
                r-=1
                no_bot+=1
            elif temp > limit:
                r-=1
                no_bot+=1
        return no_bot