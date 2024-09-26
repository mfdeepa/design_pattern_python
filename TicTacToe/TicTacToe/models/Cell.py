from dataclasses import dataclass
from models.CellState import CellState


@dataclass
class Cell:
    row: int
    col: int
    _cell_state: CellState

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.player = None
        self._cell_state = CellState.EMPTY

    def print_cell(self):
        if self._cell_state == CellState.FILLED:
            print(f"| {self.player.symbol.symbol} |", end="")
        else:
            print("|  - |", end="")


    @property
    def cell_state(self):
        return self._cell_state

    @cell_state.setter
    def cell_state(self, cell_state):
        self._cell_state = cell_state

    def print_cell(self):
        if self._cell_state == CellState.FILLED:
            print(f"| {self.player.symbol.symbol} |", end="")
        else:
            print("|  - |", end="")
