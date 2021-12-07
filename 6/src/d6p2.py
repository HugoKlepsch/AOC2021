from sys import stdin
from typing import List, Dict

from fish import LanternFish


def calc_num_fish(fishes: List[LanternFish], n_days: int):
  fish_buckets: List[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  for fish in fishes:
    fish_buckets[fish.timer] += 1

  print(f'initial fishes: {[fish_buckets[(i) % 9] for i in range(len(fish_buckets))]}')
  day = 0
  while day < n_days:
    zero_index = day % 9
    six_index = (zero_index + 6) % 9
    num_fish_breeding = fish_buckets[zero_index]
    day += 1
    zero_index = day % 9
    six_index = (zero_index + 6) % 9
    fish_buckets[six_index] += num_fish_breeding
    print(f'after {day + 1} days, fishes: {[fish_buckets[(i + day) % 9] for i in range(len(fish_buckets))]}')

  return sum(fish_buckets)


def main():
  fishes: List[LanternFish] = []

  for line in stdin:
    line = line.strip()
    if line == '':
      continue
    for timer in line.split(','):
      fishes.append(LanternFish(int(timer)))

  print(calc_num_fish(fishes, 256))


if __name__ == "__main__":
  main()
