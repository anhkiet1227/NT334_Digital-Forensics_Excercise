import googlemaps
import sqlite3
import gmplot

# Load API key
API_KEY = 'AIzaSyCh-AQDFLaIu0DeD4tamacCf5Rw3DH2D6c'

# Connect to the database
conn = sqlite3.connect('Location.db')
cursor = conn.cursor()

# Create a Google Maps client
gmaps = googlemaps.Client(key=API_KEY)

# Retrieve data from the database
cursor.execute("SELECT * FROM locations")
data = cursor.fetchall()

# Create a GoogleMapPlotter object
gmap = gmplot.GoogleMapPlotter(30.3164945, 78.03219179999999, 13, apikey=API_KEY)

# Iterate over the data and draw markers on the map
for row in data:
    date, lat, lng, color = row
    location = (lat, lng)
    
    # Define the color of the marker
    if color == 120.0:
        marker_color = 'blue'
    else:
        marker_color = 'red'
    
    # Add a marker to the map
    gmap.marker(location[0], location[1], color=marker_color)


# Save the map to an HTML file
gmap.draw('map.html')

# Close the database connection
conn.close()