class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        total_count = [1000000]*26

        for s in words:
            current_count = [0]*26
            for c in s:
                current_count[ord(c)-ord('a')]+=1
            for c in range(26):
                total_count[c] = min(total_count[c],current_count[c])

        results = []
        for c in range(26):
            for _ in range(total_count[c]):
                results.append(chr(c+ord('a')))
        return results

        