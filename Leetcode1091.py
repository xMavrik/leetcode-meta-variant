"""
Given an n x n binary matrix grid, return the shortest path. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.


Input: grid = [[0,1],[1,0]]
Output: 2



Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: [[0, 0], [0, 1], [1, 2], [2, 2]]


"""

from collections import deque


def shortestPathBinaryMatrix(grid):
        
        if not grid:
            return -1

        if grid[0][0] != 0:
            return -1
        
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1], [-1, 1], [1, -1], [1, 1], [-1, -1]]
        
        q = deque([[0, 0, [[0, 0]]]])

        grid[0][0] = 1

        while q:

            current_x, current_y, path_list = q.popleft()

            if current_x == len(grid) - 1 and current_y == len(grid[0]) - 1:
                return path_list

            for dx, dy in directions:

                mod_x = current_x + dx
                mod_y = current_y + dy

                if 0 <= mod_x < len(grid) and 0 <= mod_y < len(grid[0]) and grid[mod_x][mod_y] == 0:
                    grid[mod_x][mod_y] = 1
                    path_copy = path_list[:]
                    path_copy.append([mod_x, mod_y])
                    q.append([mod_x, mod_y, path_copy])

        return -1

grid1 = [[0,0,0],[1,1,0],[1,1,0]]

#print(shortestPathBinaryMatrix(grid1))


"""
Sometimes, DFS is faster than BFS, if we want to return ANY path, DFS is way faster since we just need to go deep instead of going wide
"""

def shortestPathBinaryMatrixDFS(grid):

    if not grid:
        return -1

    if grid[0][0] != 0:
        return -1
    
    path = []

    directions = [[-1, 0], [0, -1], [1, 0], [0, 1], [-1, 1], [1, -1], [1, 1], [-1, -1]]

    #--------------------------------------
     
    def dfs(grid, path, x, y):
         
        grid[x][y] = 1
        path.append([x, y])

        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            return True
        
        for dx, dy in directions:

            mod_x = x + dx
            mod_y = y + dy

            if 0 <= mod_x < len(grid) and 0 <= mod_y < len(grid[0]) and grid[mod_x][mod_y] == 0:
            
                if dfs(grid, path, mod_x, mod_y):
                    return True
        
        path.pop()
        return False
    
    #--------------------------------------

    dfs(grid, path, 0, 0)

    return path

grid1 = [[0,0,0],[1,1,0],[1,1,0]]

print(shortestPathBinaryMatrixDFS(grid1))
