
# is it a mapping of letters to other letters
# like a cipher?

# yes but it's behind an incomplete / contradictory list of words


# can map a letter to a list of letters that are lex smaller

# and then if contradictions are present return ""

# dfs through this mapping to find the correct path down that doesn't contradict?



# can return early if in the map, a smaller lex is found where it can't be



class Solution:
    def foreignDictionary(self, words: List[str]) -> str:


        # keys are all chars in all words
        # vals are sets of all chars lex smaller than the key
        relations = {c: set() for word in words for c in word}

        last = None

        for word in words:
            if last is not None:
                for i in range(min(len(word), len(last))):
                    
                    # last is lex smaller than word
                    if word[i] != last[i]:
                        relations[word[i]].add(last[i])
                        break
                else:
                    # the loop didn't find an unmatching char
                    # if the words are diff lengths
                    # could be invalid lex
                    if len(word) < len(last):
                        return ""
            
            last = word
        
                    
        
        # build the string, backtrack on invalid lex
        def dfs(c):
            
            if self.visited[c] == True:
                return
            
            if self.visited[c] == False:
                # currently checking this path
                # so cycle exists, and lex is invalid
                return True

            # = none
            self.visited[c] = False
            for nei in relations[c]:

                if dfs(nei) == True:
                    return True
            
            self.visited[c] = True
                
            self.result += c 
            

            



        self.visited = {c: None for word in words for c in word}
        self.result = ""

        for c in relations.keys():
            if dfs(c) == True: return ""

        

        return self.result





        