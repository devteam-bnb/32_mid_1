from collections import deque

# Moves: up, down, left, right
moves = {
    0: [1, 3],       # positions tile 0 can move to
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def bfs(start, goal):
    visited = set()
    queue = deque([(start, [])])
    
    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path + [current]
        
        visited.add(current)
        zero_index = current.index('0')
        
        for move_to in moves[zero_index]:
            new_state = list(current)
            new_state[zero_index], new_state[move_to] = new_state[move_to], new_state[zero_index]
            new_state_str = ''.join(new_state)
            
            if new_state_str not in visited:
                queue.append((new_state_str, path + [current]))

    return None

def print_board(state):
    for i in range(0, 9, 3):
        print(" ".join(state[i:i+3]))
    print()

# Input
start = input("Enter start state (e.g. 123456780): ")
goal = input("Enter goal state (e.g. 123456780): ")

# Run BFS
path = bfs(start, goal)

# Show result
if path:
    print(f"\nSteps to solve (total: {len(path)-1} moves):")
    for step in path:
        print_board(step)
else:
    print("No solution found.")