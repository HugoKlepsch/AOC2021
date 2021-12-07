class LanternFish:
  RESET_AGE = 6

  def __init__(self, timer: int = 8):
    self.timer = timer

  def pass_day(self) -> None:
    if self.timer == 0:
      self.timer = self.RESET_AGE
    else:
      self.timer -= 1

  def can_breed(self) -> bool:
    return self.timer == 0

  def __repr__(self):
    return f'{self.timer}'

