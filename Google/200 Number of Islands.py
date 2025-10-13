'''https://leetcode.com/problems/number-of-islands/description/'''

'''Logic:
1. Scan the grid row by row and column by column to find unvisited land cells '1'.
2. When a '1' is found, increment the island count since it represents a new island.
3. Use BFS (or DFS) starting from this cell to explore all connected land cells in four directions (up, down, left, right).
4. Mark each visited cell as '0' to avoid counting it again.
5. Continue scanning the grid until all cells have been checked. Each new unvisited '1' triggers the same process for the next island.'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        num_islands = 0
        
        for i in range(len(grid)): #Row
            for j in range(len(grid[0])): #Column
                if grid[i][j] == '1':
                    num_islands = num_islands + 1
                    queue = deque([(i, j)])
                    while queue:
                        x, y = queue.popleft()
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
                            grid[x][y] = '0'  # mark as visited
                            for dx, dy in directions:
                                queue.append((x + dx, y + dy))
        
        return num_islands