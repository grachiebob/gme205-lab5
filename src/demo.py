from spatial import Parcel, Building, Road

parcel = Parcel(
    p_id=101,
    zone='Commercial',
    is_active=True,
    geometry_data={
        "type": "Polygon",
        "coordinates": [[[121.050, 14.650], [121.051, 14.650], [121.051, 14.651], [121.050, 14.651], [121.050, 14.650]]]
    }
)

building = Building(
    geometry_data={
        "type": "Polygon",
        "coordinates": [[[121.052, 14.652], [121.053, 14.652], [121.053, 14.653], [121.052, 14.653], [121.052, 14.652]]]
    },
    floors=5
)

road = Road(
    geometry_data={
        "type": "LineString",
        "coordinates": [[121.050, 14.650], [121.052, 14.651], [121.054, 14.652]]
    },
    width=8
)

parcel.effective_area()
building.effective_area()
road.effective_area()

features = [parcel, building, road]
for f in features:
    print(type(f).__name__, f.effective_area())