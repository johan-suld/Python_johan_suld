from Circle import Circle
from Rectangle import Rectangle
from Sphere import Sphere
from Cuboid import Cuboid

circle1 = Circle(x=2, y=3, radius=3)
circle2 = Circle(x=0, y=0, radius=1)
rectangle1 = Rectangle(x=-1, y=-2, side1=3, side2=2)
rectangle2 = Rectangle(x=0, y=0, side1=2, side2=2)
sphere1 = Sphere(x=2, y=3, z=-1, radius=2)
sphere2 = Sphere(x=0, y=0, z=0, radius=1)
cuboid1 = Cuboid(x=-1, y=2, z=1, side1=2, side2=1, side3=3)
cuboid2 = Cuboid(x=0, y=0, z=0, side1=2, side2=2, side3=2)

def test_area_volume():
    assert round(circle1.area, 2) == 28.27
    assert rectangle1.area == 6
    assert round(sphere1.volume, 2) == 33.51
    assert cuboid1.volume == 6

def test_circumference_surface():
    assert round(circle1.circumference, 2) == 18.85
    assert rectangle1.circumference == 10
    assert round(sphere1.surface_area, 2) == 50.27
    assert cuboid1.perimeter == 22

def test_dist_from_center():
    assert circle1.dist_from_center == 3
    assert round(rectangle1.dist_from_center, 2) == 1.80

def test_unit_circle():
    assert circle1.is_unit_circle() == False
    assert circle2.is_unit_circle() == True

def test_is_square():
    assert rectangle1.is_square() == False
    assert rectangle2.is_square() == True

def test_is_unit_sphere():
    assert sphere1.is_unit_sphere() == False
    assert sphere2.is_unit_sphere() == True

def test_is_cube():
    assert cuboid1.is_cube() == False
    assert cuboid2.is_cube() == True

def test_is_inside():
    assert circle1.is_inside(point_x=1.8, point_y=2.9) == True
    assert circle2.is_inside(point_x=-2, point_y=-3.1) == False
    assert rectangle1.is_inside(point_x=0.8, point_y=1) == False
    assert rectangle2.is_inside(point_x=-0.5, point_y=0.5) == True
    assert sphere1.is_inside(point_x=3, point_y=2, point_z=1) == False
    assert sphere2.is_inside(point_x=0.2, point_y=0.1, point_z=0.3) == True
    assert cuboid1.is_inside(point_x=-0.5, point_y=2.2, point_z=0) == True
    assert cuboid2.is_inside(point_x=3, point_y=1, point_z=1) == False

test_area_volume()
test_circumference_surface()
test_dist_from_center()
test_unit_circle()
test_is_square()
test_is_unit_sphere()
test_is_cube()
test_is_inside()