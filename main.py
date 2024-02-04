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


def bfs(maze, start, goal):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start, [])])
    visited = set()
    while queue:
        current, path = queue.popleft()
        x, y = current
        if current == goal:
            return path + [current]
        if current in visited:
            continue
        visited.add(current)
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and (maze[new_x][new_y] == "🔘" or maze[new_x][new_y]=="S" or maze[new_x][new_y]=="E"):
                queue.append(((new_x, new_y), path + [current]))
    return None


def main():
    print("🥳-----WELCOME TO MAZE SOLVER-----🥳")
    n=int(input("Enter the Maze Size:- "))
    rows, cols = n, n  # Adjust the maze size as needed
    
    
    
    percent_to_remove = int(input("put the parcent of wall in maze (0-25)%:- "))
    
   
    print()
    while True:
        print("------choose the number------")
        print("1.Generate the Maze and print it")
        print("2.Print the Path")
        print("3.Exit the game")
        user_input=int(input("choose above any input process:- "))
        if user_input==1:
            maze = generate_maze(rows, cols,percent_to_remove)
            maze[0][0]="S"
            maze[-1][-1]="E"
          
            # remove_walls(maze, percent_to_remove)
            print("Generated Maze:👇")
            print_maze(maze)
        if user_input==2:
            start = (0, 0)
            goal = (n-1, n-1)
            # Find the shortest path using BFS
            shortest_path = bfs(maze, start, goal)
            # print(shortest_path)
        
            if shortest_path:
                for tup in shortest_path:
                    i=tup[0]
                    j=tup[1]
                    maze[i][j]="🟢"
                print_maze(maze)
                # print("Shortest path:")
            else:
                print("_-----🥺No path found💔----.")
                
        if user_input==3:
            print("-----🤩 thank you for playing game🤩----")
            return 
    # print(maze)
    

if __name__ == "__main__":
    main()
