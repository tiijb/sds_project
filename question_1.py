import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import requests

#Access and load the züri wie neu data via API

url_zwn = "https://www.ogd.stadt-zuerich.ch/wfs/geoportal/Zueri_wie_neu?service=WFS&version=1.1.0&request=GetFeature&outputFormat=GeoJSON&typename=zwn_meldungen_p"
response_zwn = requests.get(url_zwn)
if response_zwn.status_code == 200:
    print("Data züri wie neu loaded sugessfull")
    zurich_zwn_gdf = gpd.read_file(response_zwn.url)
else:
    print("Data züri wie neu loading failed")

#Access and load the neighbourhood data via API

url_neighbourhoods = "https://www.ogd.stadt-zuerich.ch/wfs/geoportal/Statistische_Quartiere?service=WFS&version=1.1.0&request=GetFeature&outputFormat=GeoJSON&typename=adm_statistische_quartiere_map"
response_neighbourhoods = requests.get(url_neighbourhoods)
if response_neighbourhoods.status_code == 200:
    print("Data neighbourhood loaded sugessfull")
    zurich_neighbourhoods_gdf = gpd.read_file(response_neighbourhoods.url)
else:
    print("Data neighbourhood loading failed")


#Access and load the income data via API

url_income = url = 'https://data.stadt-zuerich.ch/api/3/action/datastore_search?resource_id=af01ed91-04f8-445b-8dfc-04cbf0a27e95&limit=5&q=title:jones'
response_income = requests.get(url_income)
if response_income.status_code == 200:
    print("Data Income loaded sugessfull")

    #convert the json response into a dictionary
    zurich_income_dic = response_income.json()
    #convert the dictionary into a dataframe
    zurich_income_df = pd.DataFrame(zurich_income_dic)
else:
    print("Data income loading failed")

