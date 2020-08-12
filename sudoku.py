"""
This small program solves SUDOKU puzzles
"""

__author__ = "Alejandro Perez-Mendez"
__copyright__ = "Copyright 2020, The Cogent Project"
__license__ = "BSD"
__version__ = "0.1"
__email__ = "alejandro.perez.mendez@gmail.com"


class State(object):
    def __init__(self, values):
        """
        Creates a new state cloning from a 2-dimensional array
        """
        self.values = [row[:] for row in values]

    @classmethod
    def from_string(cls, string):
        """
        Creates a new state from a 81 character string
        """
        string = string.replace(' ', '')
        values = []
        for base in range(0, 81, 9):
            values.append([int(x) for x in string[base:base+9]])
        return State(values)

    def is_solved(self):
        """
        Returns whether this State represents a solved game
        """
        return not any(0 in row for row in self.values)

    def get_used_numbers(self, x1, y1, x2, y2):
        """
        Returns a set of used numbers in the indicated sub-matrix
        """
        used = set()
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                value = self.values[i][j]
                if value != 0:
                    used.add(value)
        return used

    def get_available_numbers(self, i, j):
        """
        Returns the set of numbers that could be used for the indicated position
        """
        available = set(range(1, 10))
        # Remove any number that is already in this row
        available -= self.get_used_numbers(i, 0, i, 8)
        # Remove any number that is already in this column
        available -= self.get_used_numbers(0, j, 8, j)
        # remove any number that is already in this 3x3 quadrant
        quadranti = 3 * (i // 3)
        quadrantj = 3 * (j // 3)
        available -= self.get_used_numbers(quadranti, quadrantj, quadranti + 2, quadrantj + 2)
        return available

    def generate_states(self):
        """
        Generates possible states from the current one
        """
        newstates = []
        for i in range(9):
            for j in range(9):
                if self.values[i][j] == 0:
                    for val in self.get_available_numbers(i, j):
                        newstate = State(self.values)
                        newstate.values[i][j] = val
                        newstates.append(newstate)
                    return newstates
        return []

    def __str__(self):
        result = ''
        for row in self.values:
            result += ' '.join(str(x) for x in row) + '\n'
        return result


def main():
    # initial state. 0s represent empty values
    initial = State.from_string('1 3 0 9 0 5 0 2 0'
                                '0 5 7 2 0 6 1 0 0'
                                '0 6 2 1 0 4 0 0 7'
                                '5 7 3 8 0 0 2 0 0'
                                '0 8 0 4 2 7 0 3 0'
                                '0 0 1 5 6 3 8 7 0'
                                '0 9 0 0 0 0 4 6 0'
                                '8 0 0 6 5 9 0 1 0'
                                '7 1 0 0 4 0 9 8 0')

    states = [initial]
    iterations = 0
    while states:
        iterations += 1
        state = states.pop()
        if state.is_solved():
            print("Game solved in {} iterations".format(iterations))
            print(state)
            return
        else:
            states += state.generate_states()


if __name__ == "__main__":
    main()
