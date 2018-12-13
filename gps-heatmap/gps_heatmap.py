import pandas as pd
import folium
from folium.plugins import HeatMap
import os

# data_file = 'data/gps.tsv'
data_file = 'demo.tsv'

for_map = pd.read_csv(data_file, sep='\t')
for_map.sort_values('Amount', ascending=False).head()
for_map.info()

max_amount = float(for_map['Amount'].max())

hmap = folium.Map(location=[21.0, 105.3], zoom_start=7, tiles="OpenStreetMap")

hm_wide = HeatMap( list(zip(for_map.lat.values, for_map.lon.values, for_map.Amount.values)),
                   min_opacity=0.2,
                   max_val=max_amount,
                   radius=10, blur=15,
                   max_zoom=1,
                 )

hmap.add_child(hm_wide)
hmap.save(os.path.join('results', 'geo_heatmap.html'))