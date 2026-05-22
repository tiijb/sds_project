## This File contains all the functions for loading the data of the züri wie neu project

import requests
import geopandas as gpd
import pandas as pd


### import geografic data function

url_zwn = "https://www.ogd.stadt-zuerich.ch/wfs/geoportal/Zueri_wie_neu?service=WFS&version=1.1.0&request=GetFeature&outputFormat=GeoJSON&typename=zwn_meldungen_p"
def import_geografic_data(url):
    """loads the geographic data as a geodataframe
    
    This function loads the geografic data from a given url into a geodataframe and converts it the LV95 coordinates
    if it is successfull it prints 'data loaded successfully' and returns the data,
    otherwise it prints 'data loading failed'
    
    parameters
    ------------
    url: a url to a geografic data file that is compatible with gpd.read_file()
    
    outputs
    ------------
    success: a geodataframe containing the data
    failed: no output"""
    
    try:
        gdf = gpd.read_file(url).to_crs(epsg="2056")
        print("data loaded successfully")
        return gdf
    except:
        print( "data loading failed")



# import data function

def import_data(url):
    """imports the data as a dataframe from the given CKAN API URL
    
    This function loads the data from a given CKAN API URL into a dataframe
    if it is successfull it prints 'data loaded successfully' and returns the data,
    otherwise it prints 'data loading failed'
    
    parameters
    ------------
    url: a CKAN API URL to a data file
    
    outputs
    ------------
    success: a dataframe containing the data
    failed: no output"""

    response_population = requests.get(url)
    if response_population.status_code == 200:
        print("data loaded successfully")

        #convert the json response into a dictionary (because the CKAN API returns a new dictionary where the data is in result and record)
        population_dic = response_population.json()["result"]["records"]
        #convert the dictionary into a dataframe
        population_df = pd.DataFrame(population_dic)
        return population_df
    else:
        print("data loading failed")

