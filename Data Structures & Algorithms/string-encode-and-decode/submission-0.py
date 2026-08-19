
class Solution:

    def encode(self, strs: List[str]) -> str:

        accume = ""
        for s in strs:
            accume += str(len(s)) + "#" + s
        return accume

    def decode(self, s: str) -> List[str]:

        decoded_words = []
        i = 0

        while i < len(s):

            j = i
            while s[j] != "#":
                j += 1
            
            # Now j at next #

            # from i to j is int length

            word_length = int(s[i:j])

            start_word = j + 1
            end_word = start_word + word_length

            decoded_words.append(s[start_word:end_word])

            i = end_word

        return decoded_words
                








        

        


            
