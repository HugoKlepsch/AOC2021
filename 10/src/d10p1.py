from collections import defaultdict
from sys import stdin
from typing import List, Dict, Set, Tuple


def main():

  score: int = 0
  for line in stdin:
    line = line.strip()
    if line == '':
      continue
    stack: List[str] = []
    openers: Dict[str] = {
      '[': ']',
      '{': '}',
      '(': ')',
      '<': '>',
    }
    closers: Set[str] = {']', '}', ')', '>'}
    point_map = {
      ')': 3,
      ']': 57,
      '}': 1197,
      '>': 25137,
    }
    for c in line:
      if c in openers:
        stack.append(openers[c])
      elif c in closers:
        top = stack.pop()
        if c != top:
          print(f'invalid char {c}, expected {top}')
          score += point_map[c]
          break
  print(f'Score: {score}')


if __name__ == "__main__":
  main()
