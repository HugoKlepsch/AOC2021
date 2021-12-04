from sys import stdin
from typing import List

from bingo import BingoBoard


def parse_csv_line_to_numbers(line: str, sep: str = ',') -> List[int]:
  splits = line.strip().split(sep)
  return [int(s.strip()) for s in splits if s != '']


def main():

  draw_numbers = parse_csv_line_to_numbers(stdin.readline())
  bingo_boards: List[BingoBoard] = []
  for line in stdin:
    line = line.strip()
    if line == '':
      continue

    first_line = parse_csv_line_to_numbers(line, ' ')
    board = [first_line]
    size = len(first_line)

    # size - 1 because we already read the first line
    for i in range(size - 1):
      board.append(parse_csv_line_to_numbers(stdin.readline(), ' '))
    bingo_boards.append(BingoBoard(board))

  for drawn_number in draw_numbers:
    found_winner = False
    for board in bingo_boards:
      if board.draw_number(drawn_number):
        score = board.score(drawn_number)
        print(f'score: {score}')
        found_winner = True
        break
    if found_winner:
      break


if __name__ == "__main__":
  main()
