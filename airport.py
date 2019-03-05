
class Airport():
  def __init__(self, capacity = 10):
    self.hangar = []
    self.capacity = capacity

  def land(self, plane):
    self.hangar.append(plane)

  def takeoff(self, plane):
    self.hangar.pop(0)