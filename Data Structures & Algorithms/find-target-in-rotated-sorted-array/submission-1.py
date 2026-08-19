
# if nums[left] < target < nums[mid]: the target is in the sorted section between left and mid
# update right to mid

# probably determine the sorted side and side with the rotation in it first
# then second level if stmt with comps to target and updates to left + right ptrs




class Solution:
    def search(self, nums: List[int], target: int) -> int:
        



        left = 0

        right = len(nums) - 1


        while left < right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[right]:
                # Right side out of order

                # if the right side is out of order, check the in order left side (if it contains target)
                # else continue to search in the right

                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    # target is not in the sorted left side
                    # continue b search on right
                    left = mid + 1

            
            else:
                # >=, left side out of order including mid potentially

                # check sorted right side for target
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    # target is not in the sorted right side, mid inclusive
                    right = mid - 1


        # Now left or right has either landed on the target index, or if both are not target: -1
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1


        

