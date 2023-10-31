import geocoder

# Enter the location you want to find
location_name = "Statue of Liberty, New York"

# Use the geocoder to find the location
location = geocoder.osm(location_name)

if location.ok:
    print(f"Location: {location_name}")
    print(f"Latitude: {location.latlng[0]}")
    print(f"Longitude: {location.latlng[1]}")
else:
    print(f"Location '{location_name}' not found.")
Enter
