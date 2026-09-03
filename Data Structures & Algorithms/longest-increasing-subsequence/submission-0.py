
# no dupe vals

# feels like max product question

# keep track of the running max length
# either add the next or not

# track last value. if the next num is larger:
# try starting a new subsequence from that num
# and at the same time continue the current subseq. by skipping this value.
# continue skipping if needed, while the next num is larger

# is there any way for there to be a smaller subproblem in here?
# anything to memo
# 


# scan helper function that takes an index, a length of subseq, and the highest val
# (that the next value needs to be greater than (not equal to))


# if I work backward from the end of the array
# i can memo by index for ???

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)
        
        for i in range(len(nums) - 1, -1, -1):

            if i == len(nums) - 1:
                continue
            
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        
        m = dp[0]

        for v in dp:
            if v > m:
                m = v
        
        return m
