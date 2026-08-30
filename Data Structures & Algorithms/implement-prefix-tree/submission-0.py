
class TrieNode:

    def __init__(self):
        # maps letters present in the trie at this level to the next TrieNode
        self.hm = {}
        self.isWord = False


class PrefixTree:

    # Each node is a character, and the children are in a-
    # use a hm at each node to map letters to the array of 

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:

        i = 0
        last_node = self.root

        while i < len(word):

            if word[i] in last_node.hm:
                # walk to next node, where we check word[i + 1]
                last_node = last_node.hm[word[i]]
                i += 1
            else:
                # 1. add word[i] to the current trie node
                last_node.hm[word[i]] = TrieNode()
                
                # 2. move to this new node
                last_node = last_node.hm[word[i]]

                # 3. incr i
                i += 1
        
        last_node.isWord = True


    def search(self, word: str) -> bool:

        i = 0
        last_node = self.root

        while i < len(word):
            if word[i] in last_node.hm:
                last_node = last_node.hm[word[i]]
                i += 1
            else:
                return False
        
        # we made it the length of the word down the tree
        # without finding a node without the next char in it
        # so the word is in the trie

        # this must be the last node (leaf) for the word to be in the trie
        return last_node.isWord
            
    
    def startsWith(self, prefix: str) -> bool:

        # this is just search again, but without the last check for leaf node

        i = 0
        last_node = self.root

        while i < len(prefix):
            if prefix[i] in last_node.hm:
                last_node = last_node.hm[prefix[i]]
                i += 1
            else:
                return False
        
        return True

        
