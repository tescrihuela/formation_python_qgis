class Rectangle(object):
  def __init__(self, basex, basey, width, height):
    self.x = basex
    self.y = basey
    self.width = width
    self.height = height

  def get_bottom_right(self):
    d = self.x + self.width
    t = self.y + self.height
    return (d,t)

  def get_surface(self) : return (self.width * self.height)
  def get_width(self): return self.width  


rect = Rectangle(2, 4, 6, 10)
print(rect)
print(rect.get_bottom_right())
print(rect.get_width())
print("La surface est {0:.2f}".format(rect.get_surface()))
