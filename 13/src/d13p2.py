from enum import Enum
import re
from sys import stdin
from typing import List, Dict, Set, Tuple


class Bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'


class GridSetType(Enum):
  Unset = 0
  Set = 1


class Grid:
  def __init__(self, width: int, height: int):
    self.grid: List[List[GridSetType]] = [[GridSetType.Unset for _x in range(width)] for _y in range(height)]
    self.width = width
    self.height = height

  def set_point(self, x, y, set_type: GridSetType = GridSetType.Set):
    if x < 0 or x > self.width:
      return None
    if y < 0 or y > self.height:
      return None
    existing = self.grid[y][x]
    if existing == GridSetType.Unset:
      self.grid[y][x] = set_type

  def fold_along_y(self, y: int):
    if y < self.height:
      for yi in range(y + 1, self.height):
        for xi, p in enumerate(self.grid[yi]):
          reflected_y = y - (yi - y)
          self.set_point(xi, reflected_y, p)
      self.height = y

  def fold_along_x(self, x: int):
    if x < self.width:
      for yi in range(self.height):
        for xi in range(x + 1, self.width):
          reflected_x = x - (xi - x)
          p = self.grid[yi][xi]
          self.set_point(reflected_x, yi, p)
      self.width = x

  def num_points(self) -> int:
    num = 0
    for y in range(self.height):
      for x in range(self.width):
        p = self.grid[y][x]
        if p == GridSetType.Set:
          num += 1
    return num

  def __str__(self):
    output = ''
    for y in range(self.height):
      for x in range(self.width):
        p = self.grid[y][x]
        if p == GridSetType.Set:
          output += '#'
        else:
          output += '.'
      output += '\n'
    return output


def make_grid_and_add_points(all_points: List[Tuple[int, int]]) -> Grid:
  width = max(p[0] for p in all_points) + 1
  height = max(p[1] for p in all_points) + 1
  grid = Grid(width, height)
  for point in all_points:
    grid.set_point(point[0], point[1], GridSetType.Set)
  return grid


def main():
  point_re = re.compile(r"^(\d+),(\d+)")
  fold_y_re = re.compile(r"^fold along y=(\d+)")
  fold_x_re = re.compile(r"^fold along x=(\d+)")

  all_points: List[Tuple[int, int]] = []
  grid = None
  for line in stdin:
    line = line.strip()
    if line == '':
      continue
    match = point_re.match(line)
    if match:
      x = int(match.group(1))
      y = int(match.group(2))
      all_points.append((x, y))
    else:
      match = fold_y_re.match(line)
      if match:
        y = int(match.group(1))
        if grid is None:
          grid = make_grid_and_add_points(all_points)
        grid.fold_along_y(y)
        print(grid)
        print(grid.num_points())
      else:
        match = fold_x_re.match(line)
        if match:
          x = int(match.group(1))
          if grid is None:
            grid = make_grid_and_add_points(all_points)
          grid.fold_along_x(x)
          print(grid)
          print(grid.num_points())


if __name__ == "__main__":
  main()
