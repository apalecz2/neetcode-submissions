from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums)
        if k == len(counts):
            return list(counts.keys())

        freq = [[] for _ in range(len(nums) + 1)]
        for n, f in counts.items():
            freq[f].append(n)

        results = []
        for f in range(len(freq) - 1, 0, -1):
            for n in freq[f]:
                results.append(n)
                if len(results) == k:
                    return results

        return results 



