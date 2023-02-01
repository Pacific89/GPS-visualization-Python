from gps_class import GPSVis

vis = GPSVis(data_path='data2.csv',
             map_path='map2.png',  # Path to map downloaded from the OSM.
             points=(47.08255, 15.45523, 47.08135, 15.45774)) # Two coordinates of the map (upper left, lower right)

vis.create_image(color=(0, 0, 255), width=8)  # Set the color and the width of the GNSS tracks.
vis.plot_map(output='save')

print()
