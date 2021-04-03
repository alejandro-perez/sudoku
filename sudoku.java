/**
 * This small program solves SUDOKU puzzles
 */
import java.util.*;

/*
__author__ = "Alejandro Perez-Mendez"
__copyright__ = "Copyright 2020, The Cogent Project"
__license__ = "BSD"
__version__ = "0.1"
__email__ = "alejandro.perez.mendez@gmail.com"
 */

class State {
    private int[][] values;

    /**
     * Creates a new state from a 2-dymensional array
     */
    State(int[][] values) {
        this.values = values;
    }

    /**
     * Creates a new state from a string representation
     */
    State(String string_rep) {
        this.values = new int[9][9];
        string_rep = string_rep.replace(" ", "");
        for (int i = 0; i < 81; i++) {
            this.values[i/9][i%9] = Character.getNumericValue(string_rep.charAt(i));
        }
    }

    /*
     *Creates a new state cloning another one
     */
    State(State another) {
        // Found on the Internet!
        this.values = Arrays.stream(another.values).map(int[]::clone).toArray(int[][]::new);
    }

    /*
     * Returns whether this State represents a solved game
     */
    boolean isSolved() {
        for (int i=0; i<81; i++)
            if (this.values[i/9][i%9] == 0)
                return false;
        return true;
    }

    /*
     * Returns a set of used numbers in the indicated sub-matrix
     */
    Set<Integer> getUsedNumbers(int x1, int y1, int x2, int y2) {
        Set<Integer> result = new HashSet<Integer>();
        for (int i=x1; i<=x2; i++) {
            for (int j=y1; j<=y2; j++) {
                int value = this.values[i][j];
                if (value > 0)
                    result.add(value);
            }
        }
        return result;
    }

    /*
     * Returns the set of numbers that could be used for the indicated position
     */
    Set<Integer> getAvailableNumbers(int x, int y) {
        Set<Integer> available = new HashSet<Integer>();
        // add all the numbers from 1 to 9
        for (int i=1; i<10; i++)
            available.add(i);
        // remove any number that is already this this column
        available.removeAll(this.getUsedNumbers(x, 0, x, 8));
        // remove any number that is already in this row
        available.removeAll(this.getUsedNumbers(0, y, 8, y));
        // remove any number that is already in this 3x3 quadrant
        int quadrantx = 3 * (x / 3);
        int quadranty = 3 * (y / 3);
        available.removeAll(this.getUsedNumbers(quadrantx, quadranty, quadrantx + 2, quadranty + 2));
        return available;
    }

    /*
     * Generates possible states from the current one
     */
    List<State> generateStates() {
        List<State> newStates = new ArrayList<State>();
        for (int x=0; x<9; x++) {
            for (int y=0; y<9; y++) {
                if (this.values[x][y] == 0) {
                    for (Integer val : this.getAvailableNumbers(x, y)) {
                        State newState = new State(this);
                        newState.values[x][y] = val;
                        newStates.add(newState);
                    }
                    return newStates;
                }
            }
        }
        return newStates;
    }

    /*
     * Returns the string representation of this State
     */
    public String toString() {
        String result = "";
        for (int row=0; row<9; row++) {
            for (int col=0; col<9; col++) {
                result += this.values[row][col] + " ";
            }
            result += "\n";
        }
        return result;
    }
}

class Sudoku {
    public static void main (String [ ] args) {
        State initial = new State(
            "0 0 0 4 0 9 0 8 0" +
            "2 0 5 0 1 0 3 0 0" +
            "0 6 0 0 5 0 0 7 0" +
            "3 0 0 0 0 0 0 0 2" +
            "0 7 4 0 0 0 6 1 0" +
            "6 0 0 0 0 0 0 0 8" +
            "0 2 0 0 8 0 0 5 0" +
            "0 0 1 0 9 0 4 0 3" +
            "0 4 0 5 0 1 0 0 0"
        );
        List<State> states = new ArrayList<State>();
        states.add(initial);
        int iterations = 0;
        while (!states.isEmpty()) {
            iterations++;
            State state = states.remove(states.size() - 1);
            if (state.isSolved()) {
                System.out.println(String.format("Game solved in %s iterations:\n%s", iterations, state));
                break;
            }
            states.addAll(state.generateStates());
        }
    }
}
