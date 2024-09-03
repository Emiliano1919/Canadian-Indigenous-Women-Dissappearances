from geopy.distance import geodesic
from geopy.point import Point

# Original coordinates
latitude = 52.14050798628566
longitude = -122.1378399253618
original_location = Point(latitude, longitude)

# Define the distance to move (10 km west)
distance_km = 10

# Calculate new coordinates 10 km west (bearing 270 degrees)
destination = geodesic(kilometers=distance_km).destination(original_location, bearing=270)

new_latitude = destination.latitude
new_longitude = destination.longitude

print(f"New coordinates: {new_latitude}, {new_longitude}")