import random
from collections import deque
def print_maze(maze):
    for row in maze:
        print(''.join(row))

def generate_maze(rows, cols,percent_to_remove):
    maze = [['🔘' for _ in range(cols)] for _ in range(rows)]
    
    total_space = int((rows*rows)*(percent_to_remove/100))
    
   

    for _ in range(total_space):
        x, y = random.randint(0, cols - 1), random.randint(0, rows - 1)
  
        maze[x][y] ="🧱"
    
    return maze