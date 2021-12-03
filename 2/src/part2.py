import re
from sys import stdin

class Submarine:
  def __init__(self):
    self.aim = 0
    self.depth = 0
    self.horizontal = 0

  def forward(self, x):
    self.horizontal += x
    self.depth += self.aim * x

  def down(self, x):
    self.aim += x

  def up(self, x):
    self.aim -= x


def part2():
  sub = Submarine()

  forward_re = re.compile("^forward (\d)")
  up_re = re.compile("^up (\d)")
  down_re = re.compile("^down (\d)")

  for line in stdin:
    m = forward_re.match(line)
    if m:
      x = int(m.group(1))
      sub.forward(x)

    m = up_re.match(line)
    if m:
      x = int(m.group(1))
      sub.up(x)

    m = down_re.match(line)
    if m:
      x = int(m.group(1))
      sub.down(x)

  print("sub depth: {depth}, horizontal: {horizontal}, product: {p}".format(
    depth=sub.depth, horizontal=sub.horizontal, p=sub.depth * sub.horizontal
  ))


def main():
  part2()


if __name__ == "__main__":
  main()
