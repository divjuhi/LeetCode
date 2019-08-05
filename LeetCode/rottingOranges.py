import numpy as np

def orangesRotting(grid):
	row = grid.shape[0]
	column = grid.shape[1]
	rotten = [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == 2]
	fresh =  sum(val==1 for i, row in enumerate(grid) for j, val in enumerate(row))


	minute = 0
	while rotten and fresh >0:
		new_rotten =[]
		for i,j in rotten:
			for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
				if 0<= x < row and 0 <= y <column and grid[x][y]==1:
					grid[x][y] = 2
					fresh -= 1
					new_rotten.append((x, y))
		rotten = new_rotten					
		minute += 1
	return minute if fresh ==0 else -1

grid = np.array([[2,1,1],[0,2,1],[1,0,1]])
k = orangesRotting(grid)
print(k)
