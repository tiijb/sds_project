# Züri wie neu — Waste & Littering Analysis

**Author:** Tim Berger  
**Date:** May 2026

## Description

This project analyzes the spatial distribution of reports in Züri wie neu, a website where the residents of Zürich can report damages and defects on the infrastructure of the city in different categories. It was searched for the category with the most reports, which turned out to be the waste/ collection point category. To find reasons for the waste deposit reports, spatial patterns were searched and the relationship to the population density and gastronomy locations was analyzed.


## Data Sources

All data is loaded directly from the website of the city of Zürich by calling the respective function in the notebook_utils file.  
The functions take the following WFS-URL (geodata) or CKAN API URL (non geografic data) as a parameter.
Under the source link the describtion, attributes and general information about the dataset can be found.

No local data is needed. If the data fails to load, the respective url should be checked

| Dataset | Source | URL |
|---|---|---|
|Züri wie neu: Contains all the reports and their attributes and geometry of the Züri wie neu website|https://data.stadt-zuerich.ch/dataset/geo_zueri_wie_neu|https://www.ogd.stadt-zuerich.ch/wfs/geoportal/Zueri_wie_neu?service=WFS&version=1.1.0&request=GetFeature&outputFormat=GeoJSON&typename=zwn_meldungen_p|
|neighbourhoods: Contains the neighbourhoods of Zürich with attributes and geometry| https://data.stadt-zuerich.ch/dataset/geo_statistische_quartiere | https://www.ogd.stadt-zuerich.ch/wfs/geoportal/Statistische_Quartiere?service=WFS&version=1.1.0&request=GetFeature&outputFormat=GeoJSON&typename=adm_statistische_quartiere_v |
|neighbouhood labels: Contains the ideal label position of the neighbourhood labels in Zürich | https://data.stadt-zuerich.ch/dataset/geo_statistische_quartiere | https://www.ogd.stadt-zuerich.ch/wfs/geoportal/Statistische_Quartiere?service=WFS&version=1.1.0&request=GetFeature&outputFormat=GeoJSON&typename=adm_statistische_quartiere_b_p |
| population: Contains the population per neighbourhood of Zürich | https://data.stadt-zuerich.ch/dataset/bev_bestand_jahr_quartier_od3240 | https://data.stadt-zuerich.ch/api/3/action/datastore_search?resource_id=9f9e2f24-96a7-4542-843c-52d44a904110&limit=10000 |
| gastronomy: Contains all the locations with a gastronomy licence in Zürich  | https://data.stadt-zuerich.ch/dataset/geo_gastwirtschaftsbetriebe | https://www.ogd.stadt-zuerich.ch/wfs/geoportal/Gastwirtschaftsbetriebe?service=WFS&version=1.1.0&request=GetFeature&outputFormat=GeoJSON&typename=gastwirtschaftsbetriebe


## Dependencies

The external packages which are required to run the notebooks are all inside the environment sds210 which is located in the sds210_project folder.

To recreate the environment:
1. Ensure you have Conda installed.
2. Navigate to the extracted sds210_project folder: `cd <path-to-sds210-repository-folder>`
2. Then run: `conda env create -f environment.yml`
3. Activate: `conda activate zurich-heat-env`

## Execution Order

All the Notebooks are independent of each other and can be run in any order. 
However to reconstruct to workflow that has been done, the notebooks should be executed in the following order:
- category_analysis
- heatmap
- waste_neighbourhood_map
- gastronomy waste

The notebook_utils file always has to be loaded in the same folder as the the notebooks.

## Results

The produced maps and graphes are automaticaly saved to `figures`.
The following Result are Produced:
- category analysis: Barplot comparing the number of reports per category 
- heatmap: A heatmap of the reports in the waste category
- waste_neighbourhood_map: A choropleth map showing the waste reports per resident for the neighbourhoods of Zürich
- gastronomy_waste: A Barplot and Scatterplot both comparing the waste reports per resident with the gastronomy location density  
                     