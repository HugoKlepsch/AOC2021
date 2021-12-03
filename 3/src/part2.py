from collections import defaultdict
from sys import stdin


def get_bitstrings(lines):
  report_column_counts = defaultdict(lambda: defaultdict(int))
  gamma_bitstring = ''
  epsilon_bitstring = ''
  for line in lines:
    line_i = 0
    for c in line:
      report_column_counts[line_i][int(c)] += 1
      line_i += 1
    gamma_bitstring = ''
    epsilon_bitstring = ''
    for col in report_column_counts.keys():
      if report_column_counts[col][0] > report_column_counts[col][1]:
        gamma_bitstring += '0'
        epsilon_bitstring += '1'
      else:
        gamma_bitstring += '1'
        epsilon_bitstring += '0'
  return gamma_bitstring, epsilon_bitstring


def filter_ratings(ratings, bitstring, bit_i):
  return [
    r for r in ratings
    if r[bit_i] == bitstring[bit_i]
  ]


def part2():
  all_lines = []
  for line in stdin:
    line = line.strip()
    all_lines.append(line)

  o2_lines = all_lines[:]
  bit_i = 0
  while len(o2_lines) != 1:
    (gamma_bitstring, epsilon_bitstring) = get_bitstrings(o2_lines)
    o2_lines = filter_ratings(o2_lines, gamma_bitstring, bit_i)
    bit_i += 1
  o2 = int(o2_lines[0], 2)
  print(f'o2: {o2}')

  co2_lines = all_lines[:]
  bit_i = 0
  while len(co2_lines) != 1:
    (gamma_bitstring, epsilon_bitstring) = get_bitstrings(co2_lines)
    co2_lines = filter_ratings(co2_lines, epsilon_bitstring, bit_i)
    bit_i += 1
  co2 = int(co2_lines[0], 2)
  print(f'co2: {co2}')

  print(f'product: {co2 * o2}')


def main():
  part2()


if __name__ == "__main__":
  main()
