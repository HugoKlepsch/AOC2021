from collections import defaultdict
from sys import stdin


def part1():
  report_column_counts = defaultdict(lambda: defaultdict(int))
  for line in stdin:
    line = line.strip()
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

  print(f'gamma:   {gamma_bitstring}')
  print(f'epsilon: {epsilon_bitstring}')
  gamma = int(gamma_bitstring, 2)
  epsilon = int(epsilon_bitstring, 2)
  product = gamma * epsilon
  print(f'product: {product}')


def main():
  part1()


if __name__ == "__main__":
  main()
