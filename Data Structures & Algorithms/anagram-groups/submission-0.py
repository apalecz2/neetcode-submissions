
# Checking if anagram is O(length) time and space

# How can this be done where each string doesn't need to be compared against all else?

# Process each string once

# Probably some odd property. Like processing each string and adding to a shared counter which is O(1) space
# I guess counter is O(1) still since it's lowercase characters again -> which for m strings is O(m) -> target


# once i have counts then what? 
# can i take the hashmap as a string of the counts somehow? like 0,10,2,..., then match with that???
#   building these is O(1) since always length of 26, same with string matching.
#   this is just so i can compare counts

# how can i go from string comparators to groups in linear time over m?

# iterate over strings and their count strings.
#   create hashmap with count string as key, and value as array of word indices
#       this is O(m * 26 * n) space??
#       yes, but m 

# 


# 1. Create dictionary for groups
# 2. Process each string and form a counter array for each
# 3. Convert array to tuple, as key in dictionary, append original string to that keys list
# 4. Then iterate over the items in the dictionary to form return list


from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        counts = defaultdict(list)

        for i in range(len(strs)):

            count = [0] * 26
            for c in strs[i]:
                count[ord(c) - ord('a')] += 1
            
            tuple_rep = tuple(count)
    
            counts[tuple_rep].append(strs[i])

        return_list = []
        for key, value in counts.items():
            return_list.append(value)

        return return_list
        












        