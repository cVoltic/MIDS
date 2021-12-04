# A Marbles Game
# A Marbles Game - Problem
# Cuong Trinh

class MarblesBoard():
    def __init__(self, board):
        self.board = board
    
    def __str__(self):
        return f"{ self.board }"

    def __repr__(self):
        pass

    def switch(self):
        self.board[0], self.board[1] = self.board[1], self.board[0]

    def rotate(self):
        first_val = self.board.pop(0)
        self.board.append(first_val)
    
