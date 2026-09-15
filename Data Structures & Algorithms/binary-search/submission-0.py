class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        lo = 0 
        hi = len(nums)

        while lo < hi:

            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                hi = mid
            
            if nums[mid] < target:
                lo = mid + 1
            
        return -1
