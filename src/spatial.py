from shapely.geometry import shape
import math

class SpatialObject:

    def __init__(self, geometry_data):
        self.geometry = shape(geometry_data)

    def effective_area(self):
        """
        Return the spatial area representation of the object.
        Subclasses must implement this behavior.
        """
        raise NotImplementedError
    
    def scale(self):
        """
        Conversion from degrees to sqaure meters from Copilot
        """
        lat = self.geometry.centroid.y
        return (111000 * math.cos(math.radians(lat))) * 111000
    
class Parcel (SpatialObject):
    """
    From Lab 3
    """
    VALID_ZONES = {'Residential', 'Commercial', 'Industrial'}

    def __init__(self, p_id, zone, is_active, geometry_data):
        if zone not in self.VALID_ZONES:
            raise ValueError(f"Zone must be one of {self.VALID_ZONES}")
        super().__init__(geometry_data)
        self.p_id = p_id
        self.zone = zone
        self.is_active = is_active

    def effective_area(self):
        """
        Parcel area is the polygon area.
        Returns the area of the polygon in square map units. (float)
        """
        return self.geometry.area * self.scale()

class Building(SpatialObject):

    def __init__(self, geometry_data, floors):
        super().__init__(geometry_data)
        self.floors = floors

    def effective_area(self):
        """
        Represents total floor area
        Returns total floor area across all storeys. (float)
        """
        return self.geometry.area * self.floors * self.scale()

class Road(SpatialObject):
    def __init__(self, geometry_data, width):
        super().__init__(geometry_data)
        self.width = width
    
    def effective_area(self):
        """
        Represents road area. Uses buffer.
        Returns the estimated road surface area. (float)
        """
        lat = self.geometry.centroid.y
        width_degrees = self.width / 111000
        return self.geometry.buffer(width_degrees).area * self.scale()