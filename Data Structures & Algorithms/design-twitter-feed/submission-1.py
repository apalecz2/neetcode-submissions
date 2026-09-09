
# most recent can just be tracked by an int counter for time here, no need for time objects

# need a way to get the 10 most recent tweets and pull them from the list of users the user is following.

# how can I get better than O(n) time and not have to search linear through all tweets to get this subset?
# store them in a hashmap??

# store the tweets belonging to a user in a hashmap, to get all their tweets in constant time
# then for each account the user follows, do this, then sort, then cut to 10 recent. 

# this is nlogn time still

# ---

# for following and unfollowing, this should just be constant time to add a user to a set or remove from a set

# what other data structure could work for storing the tweets like this?
# heap? 
# binary search tree?

# we could insert sorted by time

# this makes insertion longer - so post tweet takes lg n time. It also needs to be balanced

# ----

# caching the 10 recent for each account doesn't sound right
# it would make insert take much longer, and take more space, and would cascade down in time required for 
# each dependency

# heap 

from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set) # user ids to follow ids
        self.tweetMap = defaultdict(list) # user ids to tweets as a list of tuples
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count += 1


    def getNewsFeed(self, userId: int) -> List[int]:

        # build a heap by count, pass if the item is not in the follow list for the user

        # while loop until we have 10
    
        # 1. push the most recent tweet from each user in the following list
        # 2. pop the max and add to the list
        # 3. grab the next tweet from that user and add to the heap
        # repeat

        most_recent_from_each = []
        for user in self.followMap[userId]:

            if self.tweetMap[user]:
                index = len(self.tweetMap[user]) - 1
            
                count, tweetId = self.tweetMap[user][index]
                most_recent_from_each.append((-count, tweetId, user, index))
        
        # add this users most recent

        if self.tweetMap[userId]:
            index = len(self.tweetMap[userId]) - 1
            count, tweetId = self.tweetMap[userId][index]
            most_recent_from_each.append((-count, tweetId, userId, index))
        
        
        heapq.heapify(most_recent_from_each)

        top_ten = []

        while most_recent_from_each and len(top_ten) < 10:
            count, tweetId, user, index = heapq.heappop(most_recent_from_each)
            top_ten.append(tweetId)

            if index > 0: # if the user has more tweets still
                new_count, new_tweetId = self.tweetMap[user][index - 1]

                heapq.heappush(most_recent_from_each, (-new_count, new_tweetId, user, index - 1))

        
        return top_ten

        

    def follow(self, followerId: int, followeeId: int) -> None:

        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        self.followMap[followerId].discard(followeeId)
        
