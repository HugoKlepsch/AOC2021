import copy
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


def polymerize(element_counts: defaultdict, pair_counts: defaultdict, rules: Dict[str, str]) -> Tuple[defaultdict, defaultdict]:
  new_pair_counts = copy.deepcopy(pair_counts)
  for form, count in pair_counts.items():
    if count > 0 and form in rules:
      pair_a = form[0]
      pair_b = form[1]
      new_element = rules[form]
      new_pair_counts[form] -= count
      new_pair_counts[pair_a + new_element] += count
      new_pair_counts[new_element + pair_b] += count
      element_counts[new_element] += count
  return element_counts, new_pair_counts


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

  pair_counts = defaultdict(int)
  element_counts = defaultdict(int)
  for i in range(len(poly) - 1):
    j = i + 1
    pair_a = poly[i]
    pair_b = poly[j]
    form = pair_a + pair_b
    pair_counts[form] += 1
    element_counts[pair_a] += 1
  element_counts[poly[-1]] += 1

  for i in range(40):
    element_counts, pair_counts = polymerize(element_counts, pair_counts, rules)
    print(f'step {i + 1} element_counts: {element_counts}, pair_counts: {pair_counts}')

  histogram_list = list(element_counts.items())
  histogram_list.sort(key=lambda x: x[1])
  score = histogram_list[-1][1] - histogram_list[0][1]
  print(f'score: {score}')


if __name__ == "__main__":
  main()
