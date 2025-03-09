class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        n = len(deck)
        res = [0]*n
        index_deck=0
        inde_res = 0
        q = deque(range(n))
        deck.sort()
        while index_deck < n:
            if q:
                t = q.popleft()
                res[t] = deck[index_deck]
                index_deck+=1
            if q:
                r = q.popleft()
                q.append(r)
        return res