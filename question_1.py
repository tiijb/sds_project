import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

url_neighbourhoods = "https://www.ogd.stadt-zuerich.ch/wfs/geoportal/Statistische_Quartiere?service=WFS&version=1.1.0&request=GetFeature&outputFormat=GeoJSON&typename=adm_statistische_quartiere_map"
zurich_neighbourhoods = gpd.read_file(url_neighbourhoods)
print(zurich_neighbourhoods.info())
print(zurich_neighbourhoods["qname"])

zurich_neighbourhoods.plot()

plt.show()