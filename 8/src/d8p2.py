from collections import defaultdict
from sys import stdin
from typing import List, Dict, Set


def parse_seqs(line) -> List[Set[str]]:
  return [str_to_set(seq) for seq in line.split(' ') if seq != '']


def set_to_string(a_set: Set[str]) -> str:
  chars = [c for c in a_set]
  chars.sort()
  return ''.join(chars)


def str_to_set(a_str: str) -> Set[str]:
  chars = [c for c in a_str]
  chars.sort()
  return set(chars)


"""
 aaaa 
b    c
b    c
 dddd 
e    f
e    f
 gggg
"""
segs_needed: Dict[int, Set[str]] = {
  0: str_to_set('abcefg'),
  1: str_to_set('cf'),
  2: str_to_set('acdeg'),
  3: str_to_set('acdfg'),
  4: str_to_set('bdcf'),
  5: str_to_set('abdfg'),
  6: str_to_set('abdefg'),
  7: str_to_set('acf'),
  8: str_to_set('abcdefg'),
  9: str_to_set('abcdf'),
}

len_to_digit: Dict[int, int] = {
  2: 1,
  3: 7,
  4: 4,
  7: 8,
}


def build_map(
  len_overlap: List[List[int]],
  num_map: Dict[int, str],
  seq_map: Dict[str, int],
  in_seqs: List[Set[str]]
):
  for digit, _ in enumerate(len_overlap):
    if digit in num_map:
      continue
    for seq in in_seqs:
      # Does this seq work for the given digit and the other mapped numbers?
      overlaps = True
      for digit_b, length in enumerate(len_overlap[digit]):
        if digit_b not in num_map:
          continue
        seq_b = str_to_set(num_map[digit_b])
        if len(seq.intersection(seq_b)) != length:
          overlaps = False
          break
      if overlaps:
        seq_string = set_to_string(seq)
        num_map[digit] = seq_string
        seq_map[seq_string] = digit


def main():
  len_overlap: List[List[int]] = [
    [0 for _j in range(10)]
    for _i in range(10)
  ]
  for digit, seq in segs_needed.items():
    for digit_b, seq_b in segs_needed.items():
      if digit == digit_b:
        continue
      size_overlap = len(seq.intersection(seq_b))
      len_overlap[digit][digit_b] = size_overlap

  for line in stdin:
    line = line.strip()
    if line == '':
      continue

    line_halfs = [half.strip() for half in line.split('|')]

    in_seqs = parse_seqs(line_halfs[0])
    out_seqs = parse_seqs(line_halfs[1])

    seq_map: Dict[str, int] = {}
    num_map: Dict[int, str] = {}

    for seq in in_seqs:
      size = len(seq)
      if size in len_to_digit:
        digit = len_to_digit[size]
        string = set_to_string(seq)
        num_map[digit] = string
        seq_map[string] = digit

    while len(num_map) < 10:
      build_map(len_overlap, num_map, seq_map, in_seqs)

    print(f'num_map: {num_map}')
    output = ''
    for seq in out_seqs:
      seq_string = set_to_string(seq)
      mapped_digit = seq_map[seq_string]
      output += str(mapped_digit)
    line_number = int(output)
    print(f'out_seqs: {out_seqs}')
    print(f'line_number: {line_number}')


if __name__ == "__main__":
  main()
