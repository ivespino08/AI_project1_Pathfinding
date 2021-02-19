import numpy as np

class Output:
    def __init__(self):
        self.cost = 0
        self.path = []
        self. maxNodes = 0

class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, n):
        self.queue.append(n)
        
    def dequeue(self):
        n = self.queue.pop(0)
        return n

def find_path_breath_first(start, goal, row, col, map_grid):        #Runs in O(n) time
    result = Output()
    
    q = Queue()
    visited = np.zeros((row,col),dtype=bool)
    prev = np.zeros((row,col), dtype=object)
    
    q.enqueue(start)                        #Add start to Queue
    visited[start[0], start[1]] = True
    result.maxNodes += 1
    
    while(len(q.queue) > 0):            #Standard B-f search
        v = q.dequeue()
        if v == goal:          #End when goal is reached
            break
        
        if v[0]-1 != -1 and map_grid[v[0]-1, v[1]] != 0 and not visited[v[0]-1, v[1]]:    #up
            visited[v[0]-1, v[1]] = True
            result.maxNodes += 1
            prev[(v[0]-1, v[1])] = 'below'
            q.enqueue([v[0]-1, v[1]])
            
        if v[0]+1 != row and map_grid[v[0]+1, v[1]] != 0 and not visited[v[0]+1, v[1]]:   #down
            visited[v[0]+1, v[1]] = True
            result.maxNodes += 1
            prev[(v[0]+1, v[1])] = 'above'
            q.enqueue([v[0]+1, v[1]])
            
        if v[1]-1 != -1 and map_grid[v[0], v[1]-1] != 0 and not visited[v[0], v[1]-1]:   #left
            visited[v[0], v[1]-1] = True
            result.maxNodes += 1
            prev[(v[0], v[1]-1)] = 'right'
            q.enqueue([v[0], v[1]-1])
            
        if v[0]+1 != col and map_grid[v[0], v[1]+1] != 0 and not visited[v[0], v[1]+1]:  #right
            visited[v[0], v[1]+1] = True
            result.maxNodes += 1
            prev[(v[0], v[1]+1)] = 'left'
            q.enqueue([v[0], v[1]+1])
    
    while v != start:
        if prev[v[0], v[1]] == 'below':
            result.cost += map_grid[v[0], v[1]]
            result.path.insert(0, [v[0], v[1]])
            v[0] = v[0]+1
        elif prev[v[0], v[1]] == 'above':
            result.cost += map_grid[v[0], v[1]]
            result.path.insert(0, [v[0], v[1]])
            v[0] = v[0]-1
        elif prev[v[0], v[1]] == 'right':
            result.cost += map_grid[v[0], v[1]]
            result.path.insert(0, [v[0], v[1]])
            v[1] = v[1]+1
        elif prev[v[0], v[1]] == 'left':
            result.cost += map_grid[v[0], v[1]]
            result.path.insert(0, [v[0], v[1]])
            v[1] = v[1]-1 
    
    result.path.insert(0, [v[0], v[1]])
    return cost

if __name__ == "__main__":
    map_grid = np.array([(2,4,2,1,4,5,2), (0,1,2,3,5,3,1), (2,0,4,4,1,2,4), (2,5,5,3,2,0,1), (4,3,3,2,1,0,1)])
    start = [1, 2]
    goal = [4, 3]
    row = 5
    col = 7
    cost = find_path_breath_first(start, goal, row, col, map_grid)