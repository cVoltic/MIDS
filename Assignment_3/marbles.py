# A Marbles Game
# A Marbles Game - Problem
# Cuong Trinh
import sys

class MarblesBoard():
    def __init__(self, board):
        self.board = list(board)
    
    def __str__(self):
        return f"{ ' '.join(map(str, self.board)) }"

    def __repr__(self):
        return f"MarblesBoard(({ ', '.join(map(str, self.board)) }))"

    def switch(self):
        """
            Switch the order of the first two items
        """
        self.board[0], self.board[1] = self.board[1], self.board[0]
        print(str(self))


    def rotate(self):
        """
            Move first item to the end of the list
        """
        first_val = self.board.pop(0)
        self.board.append(first_val)
        print(str(self))

    
    def solved(self):
        for i in range(1, len(self.board)):
            if self.board[i] < self.board[i-1]:
                return False
        return True


class Solver():
    def __init__(self, board):
        self.board = board
        self.total_step = 0

    def __str__(self):
        return f"total steps: {self.total_step}"

    def __repr__(self):
        return f"Solver({self.board})"

    def solve(self):
        print(str(self.board))
        is_solved = self.board.solved()

        while not is_solved:
            first_item = self.board.board[0]
            second_item = self.board.board[1]
            if first_item == 0 or second_item == 0:
                # edge case: if either first or second element is zero,
                # first item element cannot be switch with second element
                # only possible move is to rotate
                self.board.rotate()
                self.total_step += 1
            elif first_item > second_item:
                # if first element is lower than second element, switch the two
                self.board.switch()
                self.total_step += 1
            else:
                # final case when second item is bigger, 
                # check first item against final item.
                # if first item is bigger than final item, rotate,
                # board is sorted otherwise
                self.board.rotate()
                self.total_step += 1
            is_solved = self.board.solved()
        print(str(self))


def main(sequence):
    board = MarblesBoard(sequence)
    player = Solver(board)
    player.solve()


if __name__ == "__main__":
    """
        Big O Complexity for this Algorithm (Logic/Deduction):
        1) The Algorithm repeatedly call onto switch and/or rotate method until the list is sorted
        2) At each switch/rotate call, the algorithm perform a check of the current list against to see if it is sorted
            - To do this, we can either compared the current list with a sorted list, which the best case for the quickest sorting algorithm is O(NlogN), worst is O(N^2)
            - Or we can iterate through the current list to check if item(i - 1) < item(i), which the worst case is O(N)
        3) Each time the list is not sorted, we only perform 1 check between the first two elements
            - In other words, each one of this check is O(1) - constant time
            - Each switch is O(1)
            - Each rotate O(N) since every other element follow element 0 has to be shifted
            - assuming the worst case O(N)
        4) At any given state of the board, the algorithm is essentially performing:
            - (N*N + N*N + N*N + ......) = a*N^2, where a is all real numbers and only rotate is performed
            - (1*N + 1*N + 1*N + ......) = a*N, where a is all real numbers and only switch is performed

        Deduction:
            - Therefore, the algorithm has a lower bound of O(N) and an upper bound of O(N^2) in term of time complexity
            Ex: O(N): 
                given: [2,1]
                perform 1 switch and 1 check => (O(1*N)) = O(N)
                
    """

    sequence = tuple(sys.argv[1].split(","))
    sequence = [int(i) for i in sequence]
    main(sequence)
