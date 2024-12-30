from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq=dict(Counter(arr))
        # print(freq)
        seenF=set()
        for x in freq:
            if freq[x] in seenF:
                return False
            seenF.add(freq[x])
        return True