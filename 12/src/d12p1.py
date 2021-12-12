from enum import Enum
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


class Size(Enum):
  SMALL = 0
  BIG = 1


class Cave:
  def __init__(self, name: str, size: Size):
    self.name: str = name
    self.size: Size = size
    self.links: Set[Cave] = set()

  def add_link(self, cave: 'Cave') -> bool:
    if cave not in self.links:
      self.links.add(cave)
      cave.add_link(self)
      return True
    return False

  def __hash__(self):
    return 1

  def __eq__(self, other):
    return (
      self.name == other.name and
      self.size == other.size and
      self.links == other.links
    )

  def __repr__(self):
    return f'{self.name} {self.size} links: {[cave.name for cave in self.links]}'


all_paths: List[List[Cave]] = []


def traverse_caves(sequence: List[Cave]):
  latest_cave = sequence[len(sequence) - 1]
  for link in latest_cave.links:
    temp_sequence: List[Cave] = sequence[:]
    if link.name == 'end':
      temp_sequence.append(link)
      all_paths.append(temp_sequence)
    elif link in sequence:
      if link.size == Size.BIG:
        # All good
        temp_sequence.append(link)
        traverse_caves(temp_sequence)
    else:
      temp_sequence.append(link)
      traverse_caves(temp_sequence)


def main():
  all_caves: Dict[str, Cave] = {}
  start_cave: Cave = None
  end_cave: Cave = None
  for line in stdin:
    line = line.strip()
    if line == '':
      continue
    parts = line.split('-')
    node_a = parts[0]
    node_b = parts[1]
    cave_a = None
    cave_b = None
    for node in [node_a, node_b]:
      if node not in all_caves:
        is_big = node.isupper()
        size = Size.BIG if is_big else Size.SMALL
        cave = Cave(node, size)
      else:
        cave = all_caves[node]
      if node == 'start':
        start_cave = cave
      if node == 'end':
        end_cave = cave
      all_caves[node] = cave
      if cave_a is None:
        cave_a = cave
      else:
        cave_b = cave
    cave_a.add_link(cave_b)

  for cave_name, cave in all_caves.items():
    print(cave)

  traverse_caves([start_cave])
  for path in all_paths:
    print([cave.name for cave in path])

  print(f'num paths: {len(all_paths)}')


if __name__ == "__main__":
  main()
