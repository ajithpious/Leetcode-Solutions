from typing import List


class Solution:
    @staticmethod
    def countSquares(matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    res += dp[i][j]
        return res


# Checking in Console/PyCharm:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.countPrimes(n=10)
    # matrix = [[0,1,1,1], [1,1,1,1], [0,1,1,1]] -> 15
    # matrix = [[1,0,1], [1,1,0], [1,1,0]] -> 7
    print(Solve)
