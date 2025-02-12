class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        left = 0
        right = len(skill)-1
        skill.sort()
        prev = skill[left] + skill[right]
        final = 0

        while left < right:
            cur = skill[left] + skill[right]
            if prev != cur:
                return -1
            else:
                final += (skill[left] * skill[right])
            right-=1
            left+=1
            prev = cur
        return final
        