# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []
        for i in range(numRows):
            vals = [0] * (i+1)
            vals[0] = 1
            vals[-1] = 1
            rows.append(vals)
        for i in range(2, len(rows)):
            for j in range(1, len(rows[i])-1):
                print('i: ' +str(i) + ' j: ' + str(j))

                rows[i][j] = rows[i-1][j-1] + rows[i-1][j]
        return rows