from models.Board import Board
from models.Cell import Cell
from models.CellState import CellState
from models.Player import Player


class HumanPlayer(Player):

    def __init__(self, symbol, name, id, player_type):
        super().__init__(symbol, name, id, player_type)
        # self.input_func = input_func

    def validate_row_column(self, row: int, col: int, board: Board) -> bool:
        if row >= board.dimension() or row < 0:
            return False
        if col >= board.dimension() or col < 0:
            return False
        if board[row][col] == CellState.FILLED:
            return False
        return True

    def make_move(self, board):
        #print(self.name, "it is your turn to make a move , enter row col")
        print(f"{self.name()}, it's your turn to make the move, enter row and col")
        # row, col = map(int, self.input_func().split())
        row: int = int(input())
        col: int = int(input())

        while not self.validate_row_column(row, col, board):
            print(self.name, "invalid move, enter row col")
            # row, col = map(int, self.input_func().split())
            row: int = int(input())
            col: int = int(input())

        cell: Cell = board.board()[row][col]
        cell.cell_state = CellState.FILLED
        cell.player(self)
        return cell
