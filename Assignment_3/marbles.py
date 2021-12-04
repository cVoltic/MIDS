# A Marbles Game
# A Marbles Game - Problem
# Cuong Trinh

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




if __name__ == "__main__":
    board = MarblesBoard((3, 6, 7, 4, 1, 0, 8, 2, 5))
    player = Solver(board)
    player.solve()
