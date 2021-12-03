from sys import stdin

num_increasing = 0
prev_num = 10**8
for line in stdin:
  num = int(line.strip())
  if num > prev_num:
    num_increasing += 1
  prev_num = num

print(num_increasing)