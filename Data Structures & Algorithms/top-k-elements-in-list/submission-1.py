class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1

        freq = [[] for _ in range(len(nums) + 1)] 

        for n, f in counts.items():
            freq[f].append(n)

        results = []
        
        for i in range(len(freq) - 1, -1, -1):

            for j in range(len(freq[i])):

                if len(results) == k:
                    return results
                else:
                    results.append(freq[i][j])
        
        return results


