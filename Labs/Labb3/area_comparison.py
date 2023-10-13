def area_comparison(self, other, operator):
    '''Returns the result of the area comparison given the comparison operator'''

    if operator not in ['==', '!=', '>', '<', '>=', '<=']: 
        raise ValueError("operator must be one of '==', '!=', '>', '<', '>=', '<='")

    if hasattr(self, 'area') and hasattr(other, 'area'): 
        return True if eval(f'self.area {operator} other.area') else False
    else:
        raise AttributeError('GeometricShape has no property "area", only its subclasses')