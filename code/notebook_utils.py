## This File contains all the functions for loading the data of the züri wie neu project

import requests
import geopandas as gpd
import pandas as pd


### import data
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
        print("data loaded sugessfully")

        #convert the json response into a dictionary (because the CKAN API returns a new dictionary where the data is in result and record)
        population_dic = response_population.json()["result"]["records"]
        #convert the dictionary into a dataframe
        population_df = pd.DataFrame(population_dic)
        return population_df
    else:
        print("data loading failed")


## import züri wie neu data

def import_zwn_data():
    """imports the 'Züri wie neu' data as a geodataframe from the website of the city zurich"""
    url_zwn = "https://www.ogd.stadt-zuerich.ch/wfs/geoportal/Zueri_wie_neu?service=WFS&version=1.1.0&request=GetFeature&outputFormat=GeoJSON&typename=zwn_meldungen_p"
    try:
        zwn_gdf = gpd.read_file(url_zwn).set_crs(epsg="4326").to_crs(epsg="2056")
        print("'Züri wie neu' data loaded sugessfully")
        return zwn_gdf
    except:
        print( "'Züri wie neu' data loading failed")




## import neighbourhood data

def import_neighbourhood_data ():
    """imports the neighbourhood data as a geodataframe from the city of zürich"""
    url_neighbourhoods = "https://www.ogd.stadt-zuerich.ch/wfs/geoportal/Statistische_Quartiere?service=WFS&version=1.1.0&request=GetFeature&outputFormat=GeoJSON&typename=adm_statistische_quartiere_v"
    try:
        neighbourhood_gdf = gpd.read_file(url_neighbourhoods).set_crs(epsg="4326").to_crs(epsg="2056")
        print("neighbourhood data loaded sugessfully")
        return neighbourhood_gdf
    except:
        print( "neighbourhood data loading failed")


## import neighbourhood label data

def import_neighbourhood_label_data ():
    """imports the neighbourhood label data as a geodataframe from the city of zürich"""
    url_neighbourhood_labels = "https://www.ogd.stadt-zuerich.ch/wfs/geoportal/Statistische_Quartiere?service=WFS&version=1.1.0&request=GetFeature&outputFormat=GeoJSON&typename=adm_statistische_quartiere_b_p"
    try:
        neighbourhood_labels_gdf = gpd.read_file(url_neighbourhood_labels).set_crs(epsg="4326").to_crs(epsg="2056")
        print("neighbourhood label data loaded sugessfully")
        return neighbourhood_labels_gdf
    except:
        print( "neighbourhood label data loading failed")



## import the gastronomy data

def import_gastronomy_data ():
    """imports the neighbourhood data as a geodataframe from the city of zürich"""
    url_gastronomy = "https://www.ogd.stadt-zuerich.ch/wfs/geoportal/Gastwirtschaftsbetriebe?service=WFS&version=1.1.0&request=GetFeature&outputFormat=GeoJSON&typename=gastwirtschaftsbetriebe"
    try:
        gastronomy_gdf = gpd.read_file(url_gastronomy).set_crs(epsg="4326").to_crs(epsg="2056")
        print("gastronomy data loaded sugessfully")
        return gastronomy_gdf
    except:
        print("gastronomy data loading failed")



## 

def import_population_data():
    """imports the population data as a dataframe from the city of zürich"""
    url_population = 'https://data.stadt-zuerich.ch/api/3/action/datastore_search?resource_id=9f9e2f24-96a7-4542-843c-52d44a904110&limit=10000'
    parameter_population = {"resource_id":"9f9e2f24-96a7-4542-843c-52d44a904110", "limit":10000}
    response_population = requests.get(url_population, params=parameter_population)
    if response_population.status_code == 200:
        print("population data loaded sugessfully")

        #convert the json response into a dictionary (because the CKAN API returns a new dictionary where the data is in result and record)
        population_dic = response_population.json()["result"]["records"]
        #convert the dictionary into a dataframe
        population_df = pd.DataFrame(population_dic)
        return population_df
    else:
        print("population data loading failed")



def import_income_data():
    """imports the income data as a dataframe from the city of zürich"""
    
    url_income = 'https://data.stadt-zuerich.ch/api/3/action/datastore_search'
    parameter_income = {"resource_id":"af01ed91-04f8-445b-8dfc-04cbf0a27e95", "limit":3000}
    response_income = requests.get(url_income, params=parameter_income)
    if response_income.status_code == 200:
        print("income data loaded sugessfully")

        #convert the json response into a dictionary (because the CKAN API returns a new dictionary where the data is in result and record)
        income_dic = response_income.json()["result"]["records"]
        #convert the dictionary into a dataframe
        income_df = pd.DataFrame(income_dic)
        return income_df
    else:
        print("income data loading failed")
