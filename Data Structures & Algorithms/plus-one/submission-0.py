class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        string = ""

        for d in digits:
            string += str(d)
        
        

        value = str(int(string) + 1)

        new = [0] * len(value)

        for i in range(len(value)):
            new[i] = int(value[i])

        return new

