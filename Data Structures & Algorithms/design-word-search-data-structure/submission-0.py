
# trie with wildcards

class TrieNode:

    def __init__(self):
        self.hm = {}
        self.isWord = False



class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:

        curr = self.root

        for char in word:
            if char not in curr.hm:
                curr.hm[char] = TrieNode()
            curr = curr.hm[char]
        
        curr.isWord = True


    def search(self, word: str) -> bool:

        return self.walk(self.root, word, 0)




    def walk(self, node, word, i):

        # walk from this node down word

        curr = node

        while i < len(word):
            char = word[i]

            if char == ".":
                # Need to walk from all nodes in this nodes hm
                for child in curr.hm.values():
                    # start another walk with the chosen char
                    if self.walk(child, word, i + 1):
                        return True
                
                # the recursive calls will handle the rest of the strings
                # so return instead of incrementing i
                return False
            
            elif char not in curr.hm:
                # this walk reached an end where the word can't be made
                return False
            
            else:
                # Non wildcard, valid char in hm
                # continue this walk
                curr = curr.hm[char]
                i += 1
        
        # reached length of the word, without 
        return curr.isWord
        







