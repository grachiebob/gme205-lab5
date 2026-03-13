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
    
class Parcel (SpatialObject):

    VALID_ZONES = {'Residential', 'Commercial', 'Industrial'}
    """
    From Lab 3
    """

    def __init__(self, p_id, zone, is_active, geometry_data):
        if zone not in self.VALID_ZONES:
            raise ValueError(f"Zone must be one of {self.VALID_ZONES}")
        super().__init__(geometry_data)
        self.p_id = p_id
        self.zone = zone
        self.is_active = is_active


class Building(SpatialObject):

    def __init__(self, geometry_data, floors):
        super().__init__(geometry_data)
        self.floors = floors
    
class Road(SpatialObject):
    def __init__(self, geometry_data, width):
        super().__init__(geometry_data)
        self.width = width
    