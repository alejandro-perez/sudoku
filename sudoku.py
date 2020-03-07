init = [[0, 0, 5, 9, 6, 7, 3, 0, 0],
        [7, 9, 0, 0, 8, 3, 0, 4, 0],
        [0, 1, 8, 0, 4, 2, 0, 7, 0],
        [1, 0, 9, 4, 0, 8, 6, 5, 0],
        [0, 0, 4, 0, 0, 5, 1, 2, 0],
        [0, 0, 7, 6, 0, 0, 8, 0, 4],
        [9, 5, 0, 0, 3, 0, 7, 6, 8],
        [0, 0, 2, 0, 0, 0, 4, 1, 3],
        [0, 7, 0, 0, 1, 6, 0, 9, 5]]


def is_solved(state):
    return not any(0 in row for row in state)


def get_used_numbers(state, x1, y1, x2, y2):
    existing = set()
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            value = state[i][j]
            if value != 0:
                existing.add(value)
    return existing


def get_available_numbers(state, i, j):
    available = set(range(1, 10))
    available -= get_used_numbers(state, i, 0, i, 8)
    available -= get_used_numbers(state, 0, j, 8, j)
    basei = 3 * (i // 3)
    basej = 3 * (j // 3)
    available -= get_used_numbers(state, basei, basej, basei + 2, basej + 2)
    return available


def print_state(state):
    for row in state:
        print(row)


def generate_states(state):
    newstates = []
    for i in range(9):
        for j in range(9):
            if state[i][j] == 0:
                for val in get_available_numbers(state, i, j):
                    newstate = [row[:] for row in state]
                    newstate[i][j] = val
                    newstates.append(newstate)
                return newstates
    return []


def main():
    states = [init]
    solutions = []
    while states:
        state = states.pop()
        if is_solved(state):
            solutions.append(state)
        else:
            states += generate_states(state)
    print(f'Found {len(solutions)} solutions')
    for solution in solutions:
        print("Game solved")
        print_state(solution)


main()
