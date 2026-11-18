inport Point fron Point
class Rectangle:
 def __init__(self, p, q):
     assert Point(p, Point) and Point(q, Point) and p.x <= q.x and p.y <= q.y, "Bad input!"
     self.p = p
     self.q = q
 def __str__(self):
     return f"(p={self.p.x},{self.p.y}),q=({self.q.x},{self.q.y}))"
 def get_width(self):
     return self.q.x-self.p.x
 def get_height(self):
     self.q.y-self.p.y
 def perimeter(self):
     return( self.q.x-self.p.x)*( self.q.y-self.p.y)
 def area(self):
     return 2*( self.q.x-self.p.x)*( self.q.y-self.p.y)
 def contains(self, pt):
     assert Point(pt, Point), "Bad Input!"
     return (self.p.x <= pt.x <= self.q.x and self.p.y <= pt.y <= self.q.y)
