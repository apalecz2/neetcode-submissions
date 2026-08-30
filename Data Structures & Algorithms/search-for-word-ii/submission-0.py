
# so the same word cannot be used twice in a word, but can be a part of another word?

# backend is allowed to use "back".
# can a larger word use any characters from any other word?

# for each word
#   dfs on all board indices


# can be improved to do 1 dfs per element on the board
# just check at each level if the path matches a word

# is this the best we can do?
# comparing against the word list is going to be expensive

# preprocess words to organize by length, then check only words at that depth?


# build a trie with the words first to traverse down it at the same time as the dfs

# -----

# 1. Build trie from words
# 2. Start dfs from each element in the board
# 3. Based on the char, walk the trie -> no char, trim dfs
# 4. During each walk, replace the previous char with # temporarily so no chars are used twice



class TrieNode:
    def __init__(self):
        self.hm = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # takes list of words, return root node of trie with those words
    def build(self, words):

        for word in words:
            self.insert(word)

        return self.root

    def insert(self, word):

        curr = self.root

        for char in word:
            if char not in curr.hm:
                curr.hm[char] = TrieNode()
            
            curr = curr.hm[char]
        
        curr.isWord = True



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        self.board = board

        # 1. Build trie with the words list

        trie = Trie()

        trie.build(words)

        
        self.found = []

        # 2. Start dfs from each element
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, trie.root, "")
        

        return self.found
        

        

    def dfs(self, x, y, current_node, string):

        board_char = self.board[x][y]

        if board_char == "#":
            return
        
        if board_char not in current_node.hm:
            return


        word = string + board_char

        next_node = current_node.hm[board_char]

        # Case that this node and this char are a match for a word end
        if next_node.isWord:
            self.found.append(word)
            # remove this is word state so 2 paths to the same word don't add twice
            next_node.isWord = False
        

        

        temp = board_char
        self.board[x][y] = "#"

        # continue dfs in cardinal directions
        if x > 0: self.dfs(x - 1, y, next_node, word)
        if x < len(self.board) - 1: self.dfs(x + 1, y, next_node, word)
        if y > 0: self.dfs(x, y - 1, next_node, word)
        if y < len(self.board[0]) - 1: self.dfs(x, y + 1, next_node, word)

        self.board[x][y] = temp

            





        