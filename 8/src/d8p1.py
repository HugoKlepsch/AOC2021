from collections import defaultdict
from sys import stdin
from typing import List, Dict


def main():

  num_easy = 0
  for line in stdin:
    line = line.strip()
    if line == '':
      continue

    second = line.split('|')[1]
    out_seqs = [num for num in second.split(' ') if num != '']
    for seq in out_seqs:
      size = len(seq)
      if size == 2:
        # 1
        num_easy += 1
      if size == 4:
        # 4
        num_easy += 1
      if size == 3:
        # 7
        num_easy += 1
      if size == 7:
        # 8
        num_easy += 1
  print(f'num easy: {num_easy}')


if __name__ == "__main__":
  main()
