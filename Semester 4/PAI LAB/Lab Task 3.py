def water_jug_dfs(jug1, jug2, target):
    stack = [(0, 0)]  # Initial state (both jugs empty)
    visited = set()
    parent = {}  # To track the path

    while stack:
        state = stack.pop()
        a, b = state

        if state in visited:
            continue
        visited.add(state)

        # If target is reached
        if a == target or b == target:
            print_solution(state, parent)
            return True

        # Possible moves
        next_states = [
            (jug1, b),  # Fill jug1
            (a, jug2),  # Fill jug2
            (0, b),     # Empty jug1
            (a, 0),     # Empty jug2
            (a - min(a, jug2 - b), b + min(a, jug2 - b)),  # Pour from jug1 to jug2
            (a + min(b, jug1 - a), b - min(b, jug1 - a)),  # Pour from jug2 to jug1
        ]
        
        for new_state in next_states:
            if new_state not in visited:
                stack.append(new_state)
                parent[new_state] = state  # Track path

    print("No solution found.")
    return False


def print_solution(state, parent):
    path = []
    while state in parent:
        path.append(state)
        state = parent[state]
    path.append((0, 0))  # Initial state
    path.reverse()
    print("Solution path:")
    for step in path:
        print(step)

# Usage
jug1_capacity = 4
jug2_capacity = 3
target_amount = 2
water_jug_dfs(jug1_capacity, jug2_capacity, target_amount)
