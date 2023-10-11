import GeometricShape
import Circle
import Rectangle

c1 = Circle.Circle(2, 3, 3)
c2 = Circle.Circle(0, 0, 1)
r1 = Rectangle.Rectangle(-1, -2, 3, 2)
r2 = Rectangle.Rectangle(0, 0, 2, 2)

def test_area():
    assert round(c1.area, 2) == 28.27
    assert r1.area == 6

def test_circumference():
    assert round(c1.circumference, 2) == 18.85
    assert r1.circumference == 10

def test_dist_from_center():
    assert c1.dist_from_center == 3
    assert round(r1.dist_from_center, 2) == 1.80

def test_unit_circle():
    assert c1.is_unit_circle() == False
    assert c2.is_unit_circle() == True

def test_is_square():
    assert r1.is_square() == False
    assert r2.is_square() == True

def test_is_inside():
    assert c1.is_inside((1.8, 2.9)) == True
    assert c2.is_inside((-2, -3.1)) == False
    assert r1.is_inside((0.8, 1)) == False
    assert r2.is_inside((-0.5, 0.5)) == True

test_area()
test_circumference()
test_dist_from_center()
test_is_square()
test_is_inside()