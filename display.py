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