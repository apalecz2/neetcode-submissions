class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2

            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid
            else:
                return mid
            
        return -1
