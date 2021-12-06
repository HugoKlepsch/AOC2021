import re
from sys import stdin
from typing import List

from line import Point, Line


def main():
  line_re = re.compile(r"^([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)")
  lines: List[Line] = []

  for line in stdin:
    line = line.strip()
    if line == '':
      continue
    match = line_re.match(line)
    if match:
      p1 = Point(int(match.group(1)), int(match.group(2)))
      p2 = Point(int(match.group(3)), int(match.group(4)))
      lines.append(Line(p1, p2))

  max_y = max((
    p.y
    for line in lines
    for p in line
  ))
  max_x = max((
    p.x
    for line in lines
    for p in line
  ))

  covered_points: List[List[int]] = []
  for y in range(max_y + 1):
    covered_points.append([])
    for x in range(max_x + 2):
      covered_points[y].append(0)

  for line in lines:
    covered = line.get_covered_points(diagonals=True)
    for p in covered:
      covered_points[p.y][p.x] += 1

  points_above_2: List[Point] = []
  output = ''
  for y, line in enumerate(covered_points):
    for x, num_coverings in enumerate(line):
      if num_coverings >= 2:
        points_above_2.append(Point(x, y))
      output += '.' if num_coverings == 0 else f'{num_coverings}'
    output += '\n'

  print(output)
  print(f'Num points >= 2: {len(points_above_2)}')


if __name__ == "__main__":
  main()
