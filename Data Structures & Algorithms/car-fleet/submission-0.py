
# feels like a queue

# based on contstraints we need O(n) time

# any time a car catches up to another, merge them

# walk steps until there's no cars left

# enqueue everything, then walk steps -> O(n^2) - no go

# process once. get the time it takes to reach the destination for a car. no cause it's limited by the car in front
# well take that into account given that it will take longer or as long as the next car forward

# new array of arrival times in this manner
# group? by arrival time?

# O(n) time, O(n) space - although I could modify position in place to just be arrival time
# or just track the last time
# if this arrival time is later, discard that arrival time, and increment a counter
# which gives O(1) extra space

# this only works if it's sorted by starting position?
# for this memory optimization


# since it's unordered, each calculation for the arrival time needs to be able to be updated

# heap?



class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # 1. Pair positions and speeds together, sort by starting pos desc

        paired = [0] * len(position)
        for i in range(len(position)):
            paired[i] = (position[i], speed[i])
        
        paired.sort(reverse=True)

        arrivalTimes = [0] * len(paired)

        for i in range(len(paired)):
            arrivalTimes[i] = (target - paired[i][0]) / paired[i][1]
        

        fleets = 1

        curr_fleet_arrival = arrivalTimes[0]

        for i in range(1, len(arrivalTimes)):
            if arrivalTimes[i] <= curr_fleet_arrival:
                continue # a part of this fleet, the arrival time is still curr_fleet_arrival
            else:
                # if the time is after (larger) than curr_arrival, this is a new fleet
                curr_fleet_arrival = arrivalTimes[i]
                fleets += 1

        return fleets







        