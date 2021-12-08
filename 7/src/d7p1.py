from collections import defaultdict
from sys import stdin
from typing import List, Dict


def main():

  crabs: List[int] = []
  for line in stdin:
    line = line.strip()
    if line == '':
      continue
    crabs = [int(pos) for pos in line.split(',')]

  print(f'avg: {sum(crabs) / len(crabs)}')
  print(f'num crabs: {len(crabs)}')

  min_crab = min(crabs)
  max_crab = max(crabs)
  costs = defaultdict(int)
  for target in range(min_crab, max_crab):
    for crab in crabs:
      costs[target] += abs(crab - target)

  cost_tuples = [(target, cost) for target, cost in costs.items()]
  cost_tuples.sort(key=lambda x: x[1])

  print(f'lowest cost - target: {cost_tuples[0][0]}, cost: {cost_tuples[0][1]}')


if __name__ == "__main__":
  main()
