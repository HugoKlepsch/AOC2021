from typing import Iterable


class Point:
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y

  def __repr__(self):
    return f'{{x: {self.x}, y: {self.y}}}'


class Line:
  def __init__(self, p1: Point, p2: Point):
    self.p1 = p1
    self.p2 = p2

  def is_horizontal(self) -> bool:
    return self.p1.y == self.p2.y

  def is_vertical(self) -> bool:
    return self.p1.x == self.p2.x

  def is_diagonal(self) -> bool:
    delta_x = abs(self.p1.x - self.p2.x)
    delta_y = abs(self.p1.y - self.p2.y)
    return self.p1 != self.p2 and delta_x == delta_y

  def is_point_covered(self, p: Point) -> bool:
    # TODO make work for non-vertical / horizontal lines
    if self.is_vertical():
      if p.x == self.p1.x:
        if self.p1.y >= self.p2.y:
          return self.p1.y >= p.y >= self.p2.y
        else:
          return self.p2.y >= p.y >= self.p1.y
    elif self.is_horizontal():
      if p.y == self.p1.y:
        if self.p1.x >= self.p2.x:
          return self.p1.x >= p.x >= self.p2.x
        else:
          return self.p2.x >= p.x >= self.p1.x
    return False

  def get_covered_points(self, diagonals: bool = False) -> Iterable[Point]:
    if not (self.is_vertical() or self.is_horizontal()):
      if not diagonals:
        return []  # TODO
      else:
        if self.is_diagonal():
          if self.p1.y < self.p2.y:
            slope = 1
          else:
            slope = -1
          if self.p1.x < self.p2.x:
            return (
              Point(self.p1.x + i, self.p1.y + (i * slope))
              for i in range(0, (self.p2.x - self.p1.x) + 1)
            )
          else:
            slope *= -1
            return (
              Point(self.p2.x + i, self.p2.y + (i * slope))
              for i in range(0, (self.p1.x - self.p2.x) + 1)
            )
        else:
          return []

    if self.p1.x < self.p2.x:
      low_x = self.p1.x
      high_x = self.p2.x
    else:
      low_x = self.p2.x
      high_x = self.p1.x
    if self.p1.y < self.p2.y:
      low_y = self.p1.y
      high_y = self.p2.y
    else:
      low_y = self.p2.y
      high_y = self.p1.y

    return (
      Point(x, y)
      for x in range(low_x, high_x + 1)
      for y in range(low_y, high_y + 1)
    )

  def __iter__(self):
    yield self.p1
    yield self.p2

  def __repr__(self):
    return f'{{p1: {self.p1}, p2: {self.p2}}}'


