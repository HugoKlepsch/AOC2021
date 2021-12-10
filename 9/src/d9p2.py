from collections import defaultdict
from sys import stdin
from typing import List, Dict, Set, Tuple


class Point:
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  def __hash__(self):
    return 1

  def __ne__(self, other):
    return not self == other

  def __repr__(self):
    return f'{{x: {self.x}, y: {self.y}}}'


def format_heightmap(height_map: List[List[Point]]) -> str:
  output = ''
  for y, line in enumerate(height_map):
    for x, height in enumerate(line):
      output += str(height)
    output += '\n'
  return output


def format_basin(basin: Set[Point], max_x: int, max_y: int) -> str:
  output = ''
  for y in range(max_y):
    for x in range(max_x):
      p = Point(x, y)
      if p in basin:
        output += 'X'
      else:
        output += '.'
    output += '\n'
  return output


def basin_traverse(height_map: List[List[int]], basin_set: Set[Point], x: int, y: int):
  cur_location = Point(x, y)
  if cur_location in basin_set:
    return

  cur_height = height_map[y][x]
  if cur_height == 9:
    return

  basin_set.add(Point(x, y))

  if x > 0:
    # check left
    basin_traverse(height_map, basin_set, x - 1, y)
  if x < len(height_map[y]) - 1:
    # check right
    basin_traverse(height_map, basin_set, x + 1, y)
  if y > 0:
    # check up
    basin_traverse(height_map, basin_set, x, y - 1)
  if y < len(height_map) - 1:
    # check down
    basin_traverse(height_map, basin_set, x, y + 1)


def main():

  height_map: List[List[int]] = []
  basins: List[Set[Point]] = []

  for line in stdin:
    line = line.strip()
    if line == '':
      continue
    height_map.append([int(height) for height in line])

  low_points: List[Point] = []
  for y, line in enumerate(height_map):
    for x, height in enumerate(line):
      neighbors: List[int] = []
      if y > 0:
        # check up
        neighbors.append(height_map[y - 1][x])
      if y < len(height_map) - 1:
        # check down
        neighbors.append(height_map[y + 1][x])
      if x > 0:
        # check left
        neighbors.append(height_map[y][x - 1])
      if x < len(line) - 1:
        # check right
        neighbors.append(height_map[y][x + 1])
      if any(height >= neighbor for neighbor in neighbors):
        continue
      else:
        low_points.append(Point(x, y))

  for low_point in low_points:
    basin_temp: Set[Point] = set()
    basin_traverse(height_map, basin_temp, low_point.x, low_point.y)
    unique_basin = True
    for basin in basins:
      if len(basin.intersection(basin_temp)) != 0:
        unique_basin = False
        break
    if unique_basin:
      basins.append(basin_temp)

  basins.sort(key=lambda basin: len(basin))
  print(format_heightmap(height_map))
  for basin in basins:
    print(f'size: {len(basin)}, points: {basin}')
    print(format_basin(basin, len(height_map[0]), len(height_map)))

  print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
  top_three_sizes: List[int] = [len(basin) for basin in basins[-3:]]
  result = 1
  for size in top_three_sizes:
    result *= size
  print(f'final: {result}')

if __name__ == "__main__":
  main()
