
# eating rate of 1 is just sum of piles[i] over i

# O(n) to determine how many hours it takes with a given eating rate

# Probably binary search to determine the eating rate

# Results in O(nlogn) since each time we look at how many hours for a given eating rate, it's O(n)
# then we have to do that logn times to narrow down the eating rate, by cutting the search space in half

# how do we get the upper bound?

# lower bound is eating rate of 1


# upper bound from h? -> just = h?



# Need determineHours(piles, k) -> hours to eat all piles with given rate k
# Then binary search logic to narrow down this function


# if h == n, k must be max(piles)

# is the upper bound the len(piles), since the quickest to eat all piles is 1 pile per hour
# where k is the size of the largest pile (max(piles))

# 


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Get max value (largest pile) to set upper bound
        largest = float('-inf')
        for i in range(len(piles)):
            if piles[i] > largest:
                largest = piles[i]

        lower_bound = 1 #self.determineHours(piles, 1) # most hours at lowest rate (1)
        upper_bound = largest #self.determineHours(piles, largest) # least hours at highest rate


        # Binary search on k to minimize

        # looking for the first value of k that provides hours under h

        # like the next lower k provides hours > h


        while lower_bound <= upper_bound:
            
            mid = (upper_bound + lower_bound) // 2

            mid_hours = self.determineHours(piles, mid)

            if mid_hours <= h:
                # can eat in this time, look for smaller 
                upper_bound = mid - 1

            else:
                # cant eat in this time, look for larger k
                lower_bound = mid + 1
        
        # lower bound will fall out of the loop once it's larger than upper


        return lower_bound



        

    





    def determineHours(self, piles, k):

        hours = 0

        for i in range(len(piles)):
            # divide k into the pile, round up
            hours += math.ceil(piles[i] / k)
        
        return hours






