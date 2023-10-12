import numpy as np
import matplotlib.pyplot as plt
import Rectangle

class Cuboid(Rectangle.Rectangle):
    def __init__(self, x, y, z, side1, side2, side3):
        super().__init__(x, y, side1, side2)
        self.z = z
        self.side3 = side3
        self.volume = side1 * side2 * side3
        self.perimeter = side1 * side2 * 2 + side1 * side3 * 2 + side2 * side3 * 2
        self.dist_from_center = None # Behövs denna?

    @property
    def side3(self):
        return self._side3
    
    @side3.setter
    def side3(self, side3):
        if side3 <= 0:
            raise ValueError('side3 must be greater than 0')
        else:
            self._side3 = side3

    def __str__(self):
        return f'Cuboid centered at x: {self.x}, y: {self.y}, z:{self.z} and side1: {self.side1}, side2: {self.side2}, side3: {self.side3}'
    
    def __repr__(self):
        return f'Cuboid(x={self.x}, y={self.y}, z={self.z}, side1={self.side1}, side2={self.side2}, side3={self.side3})'

    def is_cube(self):
        return True if self.side1 == self.side2 == self.side3 else False
    
    def draw(self, axis=[]):
        '''https://www.geeksforgeeks.org/how-to-draw-3d-cube-using-matplotlib-in-python'''

        # Create axis
        axes = [self.side1, self.side2, self.side3]

        # Create Data
        data = np.ones(axes, dtype=bool)

        # Plot figure
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Voxels is used to customizations of the
        # sizes, positions and colors.
        ax.voxels(data, facecolors='b')

    def is_inside():
        ...