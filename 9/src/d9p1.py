from collections import defaultdict
from sys import stdin
from typing import List, Dict, Set, Tuple


def main():

  height_map: List[List[int]] = []

  for line in stdin:
    line = line.strip()
    if line == '':
      continue
    height_map.append([int(height) for height in line])

  low_points: List[Tuple[int, int]] = []
  for i, line in enumerate(height_map):
    for j, height in enumerate(line):
      neighbors = []
      if i > 0:
        # check up
        neighbors.append(height_map[i - 1][j])
      if i < len(height_map) - 1:
        # check down
        neighbors.append(height_map[i + 1][j])
      if j > 0:
        # check left
        neighbors.append(height_map[i][j - 1])
      if j < len(line) - 1:
        # check right
        neighbors.append(height_map[i][j + 1])
      if any(height >= neighbor for neighbor in neighbors):
        continue
      else:
        low_points.append((i, j))

  danger_score = 0
  for coord in low_points:
    danger_score += 1 + height_map[coord[0]][coord[1]]
  print(f'danger_score: {danger_score}')


if __name__ == "__main__":
  main()
