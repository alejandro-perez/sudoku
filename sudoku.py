init = [[0, 3, 5, 9, 2, 0, 0, 1, 0],
        [1, 0, 2, 7, 8, 0, 9, 0, 0],
        [0, 9, 0, 0, 3, 1, 6, 0, 2],
        [6, 0, 0, 0, 7, 8, 5, 0, 1],
        [0, 0, 3, 6, 1, 9, 7, 2, 0],
        [0, 0, 4, 0, 5, 0, 8, 9, 6],
        [0, 4, 1, 0, 0, 0, 2, 7, 0],
        [0, 5, 0, 1, 0, 7, 3, 4, 8],
        [0, 0, 8, 0, 0, 3, 0, 6, 0]]

init = [[2, 0 ,0, 6, 0, 9, 0, 0, 0],
        [7, 0, 0, 0, 5, 8, 0, 0, 0],
        [0, 9, 0, 1, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 4, 7, 6, 0],
        [0, 4, 9, 0, 0, 0, 1, 0, 0],
        [3, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 2, 0, 0],
        [4, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0]]

def is_solved(state):
    return not any(0 in row for row in state)

def check_repetitions(state, x1, y1, x2, y2):
    existing = set()
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            value = state[i][j]
            if value != 0 and value in existing:
                return False
            existing.add(value)
    return True

def is_valid(state):
    if not all(check_repetitions(state, 0, row, 8, row) for row in range(9)):
        return False
    if not all(check_repetitions(state, col, 0, col, 8) for col in range(9)):
        return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not check_repetitions(state, i, j, i + 2, j + 2):
                return False
    return True

def print_state(state):
    for row in state:
        print(row)

def generate_states(state):
    newstates = []
    for i in range(9):
        for j in range(9):
            if state[i][j] == 0:
                for val in range(1, 10):
                    newstate = [row[:] for row in state]
                    newstate[i][j] = val
                    if is_valid(newstate):
                        newstates.append(newstate)
                return newstates

def main():
    states = [init]
    while states:
        state = states.pop()
        if is_solved(state):
            print("Game solved")
            print_state(state)
            return
        states += generate_states(state)

main()
