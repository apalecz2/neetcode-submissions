class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # create list of vecs clockwise
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        steps = [len(matrix[0]), len(matrix) - 1]

        res = []

        r, c, d = 0, -1, 0

        while steps[d & 1]:
            for i in range(steps[d&1]):
                # walk in the direction
                r += directions[d][0]
                c += directions[d][1]
                res.append(matrix[r][c])
            # shrink step count for this direction
            steps[d&1] -= 1

            # change direction to next
            d += 1
            d %= 4
        
        return res


        