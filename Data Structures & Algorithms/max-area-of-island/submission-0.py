class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        max_area = 0
        

        def dfs(r, c):
            if r not in range(m) or c not in range(n) or grid[r][c] == 0:
                    return 0
            grid[r][c] = 0
            area = 1
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for x, y in directions:
                area += dfs(r + x,  c + y)
            return area

        for r in range(m):
            for c in range(n):
                max_area = max(max_area, dfs(r, c))

        return max_area
        