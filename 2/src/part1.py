import re
from sys import stdin

class Submarine:
  def __init__(self):
    self.depth = 0
    self.horizontal = 0

  def forward(self, x):
    self.horizontal += x

  def down(self, x):
    self.depth += x

  def up(self, x):
    self.depth -= x


def part1():
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
  part1()


if __name__ == "__main__":
  main()
