from shapely.geometry import shape

class SpatialObject:

    def __init__(self, geometry_data):
        self.geometry = shape(geometry_data)

    def effective_area(self):
        """
        Return the spatial area representation of the object.
        Subclasses must implement this behavior.
        """
        raise NotImplementedError
    