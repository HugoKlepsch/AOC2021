from collections import defaultdict
from sys import stdin
from typing import List, Dict, Set, Tuple


def main():

  scores: List[int] = []
  for line in stdin:
    score: int = 0
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
      ')': 1,
      ']': 2,
      '}': 3,
      '>': 4,
    }
    invalid = False
    for c in line:
      if c in openers:
        stack.append(openers[c])
      elif c in closers:
        top = stack.pop()
        if c != top:
          invalid = True
          break
    if not invalid:
      stack.reverse()
      stack_copy = stack[:]
      for c in stack:
        score *= 5
        score += point_map[c]
      print(f'incomplete. Remaining: {stack_copy}, score: {score}')
      scores.append(score)

  scores.sort()
  mid_score = scores[len(scores) // 2]
  print(f'mid Score: {mid_score}')


if __name__ == "__main__":
  main()
