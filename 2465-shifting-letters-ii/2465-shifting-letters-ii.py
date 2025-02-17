class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        track = [0]*(len(s)+1)
        for start,end,direction in shifts:
            if direction == 1:
                track[start]+=1
                track[end+1]-=1
            else:
                track[start]-=1
                track[end+1]+=1
        print(track)

        for i in range(1,len(track)):
            track[i] += track[i-1]
        final = []

        for i,j in enumerate(s):
            orda = ord('a')
            curr = (ord(j)-orda + track[i])%26
            res = chr(curr + orda)
            final.append(res)
        return "".join(final)