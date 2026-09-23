class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        # hm of last index of each char
        
        # iterate through string. as each char processed, check last index
        # track furthest end of current partition

        # cut once the loop reaches that furthest end

        hm = {}

        for i in range(len(s) - 1, -1, -1):
            if s[i] in hm:
                continue
            else:
                hm[s[i]] = i
        
        res = []
        size = 0
        far_end = 0

        for i in range(len(s)):
            size += 1

            far_end = max(far_end, hm[s[i]])
            
            if i == far_end:
                res.append(size)
                size = 0
        
        return res
