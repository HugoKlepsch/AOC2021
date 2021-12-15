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


def str_to_list(s: str) -> List[str]:
  return [c for c in s]


def list_to_str(l: List[str]) -> str:
  return ''.join(l)


def polymerize(poly: List[str], rules: Dict[str, str]) -> List[str]:
  new_poly: List[str] = []
  for i in range(len(poly) - 1):
    j = i + 1
    pair_a = poly[i]
    pair_b = poly[j]
    form = pair_a + pair_b
    if form in rules:
      new_element = rules[form]
    else:
      new_element = ''
    new_poly.append(pair_a)
    new_poly.append(new_element)
  new_poly.append(poly[-1])
  return new_poly


def main():
  poly: List[str] = str_to_list(stdin.readline().strip())
  rules: Dict[str, str] = {}
  rule_re = re.compile(r"^([A-Z])([A-Z]) -> ([A-Z])")
  for line in stdin:
    line = line.strip()
    if line == '':
      continue
    match = rule_re.match(line)
    if match:
      rules[match.group(1) + match.group(2)] = match.group(3)

  print(f'poly: {poly}')
  print(f'rules: {rules}')

  for i in range(10):
    poly = polymerize(poly, rules)
    print(f'step {i + 1} poly: {poly}')

  histogram = defaultdict(int)
  for element in poly:
    histogram[element] += 1
  histogram_list = list(histogram.items())
  histogram_list.sort(key=lambda x: x[1])
  score = histogram_list[-1][1] - histogram_list[0][1]
  print(f'score: {score}')


if __name__ == "__main__":
  main()
