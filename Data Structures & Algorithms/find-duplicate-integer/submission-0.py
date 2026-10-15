class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        fast, slow = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        s_slow = 0

        while slow != s_slow:
            slow = nums[slow]
            s_slow = nums[s_slow]
        
        return s_slow