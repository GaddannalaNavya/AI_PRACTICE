from collections import deque

def bfs(start_state):
    target = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    dq = deque([start_state])
    visited = {tuple(start_state): None}

    while dq:
        state = dq.popleft()

        if state == target:
            path = []
            while state:
                path.append(state)
                state = visited[tuple(state)]
            return path[::-1]

        zero = state.index(0)
        row, col = divmod(zero, 3)

        # Possible moves: up (-3), down (+3), left (-1), right (+1)
        for move in [-3, 3, -1, 1]:
            new_zero = zero + move

            # Check boundaries
            if 0 <= new_zero < 9:
                new_row, new_col = divmod(new_zero, 3)

                # Ensure it's a valid move (no wrap-around across rows)
                if abs(row - new_row) + abs(col - new_col) == 1:
                    neighbor = state[:]
                    neighbor[zero], neighbor[new_zero] = neighbor[new_zero], neighbor[zero]

                    if tuple(neighbor) not in visited:
                        visited[tuple(neighbor)] = state
                        dq.append(neighbor)

    return None

def printSolution(path):
    for state in path:
        print("\n".join(' '.join(map(str, state[i:i+3])) for i in range(0, 9, 3)), end="\n-----\n")

# Example usage
startState = [1, 3, 0, 6, 8, 4, 7, 5, 2]
solution = bfs(startState)

if solution:
    printSolution(solution)
    print(f"Solved in {len(solution) - 1} moves.")
else:
    print("No solution found.")
