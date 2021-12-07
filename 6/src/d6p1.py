from sys import stdin
from typing import List

from fish import LanternFish


def calc_num_fish(fishes: List[LanternFish], n_days: int):
  for day in range(1, n_days + 1):
    new_fishes: List[LanternFish] = []
    for fish in fishes:
      if fish.can_breed():
        new_fishes.append(LanternFish())
      fish.pass_day()
    fishes = fishes + new_fishes
  return len(fishes)


def main():
  fishes: List[LanternFish] = []

  for line in stdin:
    line = line.strip()
    if line == '':
      continue
    for timer in line.split(','):
      fishes.append(LanternFish(int(timer)))

  print(calc_num_fish(fishes, 80))


if __name__ == "__main__":
  main()
