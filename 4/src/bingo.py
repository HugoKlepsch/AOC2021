from typing import List


class BingoBoard:
  def __init__(self, board: List[List[int]]):
    self.board = board
    self.numbers: List[int] = [
      num
      for line in board
      for num in line
    ]
    self.numbers.sort()

    self.drawn_board: List[List[bool]] = [
      [False for _ in range(len(board))] for _ in board
    ]

  def draw_number(self, number: int) -> bool:
    if number in self.numbers:
      for i, line in enumerate(self.board):
        for j, num in enumerate(line):
          if number == num:
            self.drawn_board[i][j] = True
            return self.check_win()
    return False

  def check_win(self) -> bool:
    for i, line in enumerate(self.drawn_board):
      if all(line):
        return True
      if all(l[i] for l in self.drawn_board):
        return True
    return False

  def score(self, drawn_number: int) -> int:
    undrawn_numbers = [
      num
      for i, line in enumerate(self.board)
      for j, num in enumerate(line)
      if not self.drawn_board[i][j]
    ]
    return sum(undrawn_numbers) * drawn_number
