import copy
import sys
from collections import defaultdict
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


class Point:
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y

  def __hash__(self):
    return hash((self.x, self.y))

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  def __ne__(self, other):
    return not self == other

  def __repr__(self):
    return f'{{x: {self.x}, y: {self.y}}}'


def get_adjacent_points(p: Point, grid: List[List[int]]) -> List[Point]:
  points = []
  if p.x > 0:
    points.append(Point(p.x - 1, p.y))
  if p.x < len(grid[p.y]) - 1:
    points.append(Point(p.x + 1, p.y))
  if p.y > 0:
    points.append(Point(p.x, p.y - 1))
  if p.y < len(grid) - 1:
    points.append(Point(p.x, p.y + 1))
  return points


def main():
  grid: List[List[int]] = []
  y = 0
  for line in stdin:
    line = line.strip()
    if line == '':
      continue
    line_points: List[int] = []
    for x, c in enumerate(line):
      line_points.append(int(c))
    grid.append(line_points)
    y += 1

  output = ''
  for line in grid:
    for p in line:
      output += str(p)
    output += '\n'
  print(output)

  distance: Dict[Point, int] = {
    Point(xi, yi): 99999
    for yi, line in enumerate(grid)
    for xi, p in enumerate(line)
  }
  distance[Point(0, 0)] = 0
  prev: Dict[Point, Point] = {
    Point(xi, yi): None
    for yi, line in enumerate(grid)
    for xi, p in enumerate(line)
  }
  unvisited: Set[Point] = {
    Point(xi, yi)
    for yi, line in enumerate(grid)
    for xi, p in enumerate(line)
  }
  while unvisited:
    closest_item = min(((p, distance[p]) for p in unvisited), key=lambda x: x[1])
    u = closest_item[0]
    unvisited.remove(u)
    neighbors: Set[Point] = set(get_adjacent_points(u, grid)).intersection(unvisited)
    for v in neighbors:
      alt = distance[u] + grid[v.y][v.x]
      if alt < distance[v]:
        distance[v] = alt
        prev[v] = u

  print(f'distance: {distance}')
  print(f'prev: {prev}')
  bottom_right_corner = Point(len(grid[0]) - 1, len(grid) - 1)
  print(f'distance to the bottom corner: {distance[bottom_right_corner]}')


if __name__ == "__main__":
  main()
