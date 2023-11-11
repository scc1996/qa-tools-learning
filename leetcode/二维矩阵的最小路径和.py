# 动态规划
# 可以直接在二维数组上进行修改，因为值只能从上方或者左方来，所以只要记录上方和左方的最小值即可，可累加进行计算
# https://leetcode.cn/problems/minimum-path-sum/solutions/25943/zui-xiao-lu-jing-he-dong-tai-gui-hua-gui-fan-liu-c/
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for i in range(0, m):
            for j in range(0, n):
                if i == j == 0: continue
                elif i == 0: grid[i][j] = grid[i][j] + grid[i][j - 1]
                elif j == 0: grid[i][j] = grid[i][j] + grid[i - 1][j]
                else: grid[i][j] = grid[i][j] + min(grid[i][j - 1], grid[i - 1][j])
        
        return grid[m - 1][n - 1]



# 递归函数
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = []

        def min_count(rows, columns, count):
            if rows == m - 1 and columns == n - 1:
                count = count + grid[rows][columns]
                result.append(count)
                return
            else:
                if rows >= m or columns >= n:
                    return

                count = count + grid[rows][columns]
                min_count(rows + 1, columns, count)
                min_count(rows, columns + 1, count)

        min_count(0, 0, 0)
        result.sort()
        print(result[0])
        return result[0]
