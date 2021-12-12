from collections import defaultdict
from sys import stdin
from typing import List, Dict, Set, Tuple


num_flashes: int = 0
did_flash: bool = True
did_every_squid_flash: bool = False


class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'


def check_flash(energies: List[List[int]], i: int, j: int):
  if energies[i][j] > 9:
    flash(energies, i, j)


def flash(energies: List[List[int]], i: int, j: int):
  energies[i][j] = -999999999999
  global did_flash
  global num_flashes
  did_flash = True
  num_flashes += 1

  for y in range(i - 1, i + 2):
    for x in range(j - 1, j + 2):
      if y < 0 or y >= len(energies) or x < 0 or x >= len(energies[i]):
        continue
      energies[y][x] += 1
  for y in range(i - 1, i + 2):
    for x in range(j - 1, j + 2):
      if y < 0 or y >= len(energies) or x < 0 or x >= len(energies[i]):
        continue
      if y == i and x == j:
        continue
      check_flash(energies, y, x)


def iterate_step(energies: List[List[int]]):
  global did_flash
  global did_every_squid_flash
  # Increment all numbers by one
  for i, line in enumerate(energies):
    for j, energy in enumerate(line):
      energies[i][j] += 1

  # please forgive me for the sins of global variables...
  # On second thought, I'm pretty sure this iteration is not needed. Keeping this in just in case...
  did_flash = True
  while did_flash:
    did_flash = False
    for i, line in enumerate(energies):
      for j, energy in enumerate(line):
        check_flash(energies, i, j)

  output = ''
  did_every_squid_flash = True
  for i, line in enumerate(energies):
    for j, energy in enumerate(line):
      if energy < 0:
        energies[i][j] = 0
        output += f'{bcolors.FAIL}{energies[i][j]}{bcolors.ENDC}'
      else:
        did_every_squid_flash = False
        output += f'{bcolors.OKBLUE}{energy}{bcolors.ENDC}'
    output += '\n'
  return output


def main():
  energies: List[List[int]] = []
  for line in stdin:
    line = line.strip()
    if line == '':
      continue
    energies.append([int(num) for num in line])

  stepi = 0
  while not did_every_squid_flash:
    o = iterate_step(energies)
    print(f'step {stepi + 1}')
    print(o)

    print(f'num flashes: {num_flashes}')
    stepi += 1


if __name__ == "__main__":
  main()
