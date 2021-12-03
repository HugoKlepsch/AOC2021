from collections import deque
from sys import stdin

ring_buffer = deque([], maxlen=3)


def parse_line(line) -> int:
  return int(line.strip())


def sum_buffer(ring_buffer) -> int:
  sum = 0
  for item in ring_buffer:
    sum += item
  return sum


num_increasing = 0
prev_sum = 10**8
ring_buffer.append(parse_line(next(stdin)))
ring_buffer.append(parse_line(next(stdin)))
for line in stdin:
  ring_buffer.append(parse_line(line))
  sum = sum_buffer(ring_buffer)
  if sum > prev_sum:
    num_increasing += 1
  prev_sum = sum

print(num_increasing)
