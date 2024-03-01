from collections import deque

# Function to check if the given coordinates are valid and within the maze boundaries
def is_valid_move(x, y, maze):
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
        return True
    return False

# Function to find the shortest path in the maze using BFS
def solve_maze(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])

    # Visited array to keep track of visited cells
    visited = [[False] * cols for _ in range(rows)]
    visited[start[0]][start[1]] = True

    # Queue for BFS traversal
    queue = deque()
    queue.append(start)

    # Dictionary to store the parent cells for backtracking the path
    parent = {}

    # BFS traversal
    while queue:
        x, y = queue.popleft()

        # Check if we have reached the destination
        if (x, y) == end:
            break

        # Check neighboring cells
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x = x + dx
            new_y = y + dy

            if is_valid_move(new_x, new_y, maze) and not visited[new_x][new_y]:
                queue.append((new_x, new_y))
                visited[new_x][new_y] = True
                parent[(new_x, new_y)] = (x, y)

    # Backtrack the path from the destination to the start
    path = []
    curr = end
    while curr != start:
        path.append(curr)
        curr = parent[curr]
    path.append(start)

    # Reverse the path to get it from start to end
    path.reverse()

    return path

# Function to create a maze from user input
def create_maze():
    while True:
        try:
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    maze = []
    for _ in range(rows):
        while True:
            row_input = input(f"Enter a row with {cols} values (0 for empty, 1 for walls): ")
            row = row_input.split()

            if len(row) == cols:
                try:
                    row = list(map(int, row))
                    if all(val == 0 or val == 1 for val in row):
                        maze.append(row)
                        break
                    else:
                        print("Invalid values. Please enter 0 for empty or 1 for walls.")
                except ValueError:
                    print("Invalid input. Please enter 0 for empty or 1 for walls.")
            else:
                print(f"Invalid number of values. Please enter {cols} values.")

    return maze

# Function to print the maze
def print_maze(maze):
    for row in maze:
        print(' '.join(map(str, row)))

# Main function
def main():
    # Create a maze from user input
    maze = create_maze()

    print("\nMaze:")
    print_maze(maze)
    try:
        start = tuple(map(int, input("\nEnter the starting coordinates (row column): ").split()))
        end = tuple(map(int, input("Enter the ending coordinates (row column): ").split()))
    except ValueError:
        print("Invalid input. Please enter an integer.")

    # Solving the maze
    path = solve_maze(maze, start, end)

    if path:
        print("\nShortest path found:")
        for cells in path:
            print(cells)
    else:
        print("\nNo path found.")

if __name__ == "__main__":
    main()
