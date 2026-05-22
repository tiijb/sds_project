# Züri wie neu — Waste & Littering Analysis

**Author:** Tim Berger  
**Date:** May 2026

## Description

This project analysis the spatial distribution of reports in Züri wie neu, a website where the residents of Zürich can report damages and defects on the infrastructure of the city in different categories. It was searched for the category with the most reports, which turned out to be the waste/ collection point category. To find reasons for the waste deposit reports, spatial patterns were searched and the relationship to the population density and gastronomy locations was analyzed.


## Data Sources

All data is loaded directly from the website of the city of Zürich by calling the respective function in the notebook_utils file.  
The functions take the following WFS-URL (geodata) or CKAN API URL (non geografic data).
Under the source link the describtion, attributes and general information about the dataset can be found

| Dataset | Source | URL |
|---|---|---|
|Züri wie neu|https://data.stadt-zuerich.ch/dataset/geo_zueri_wie_neu|https://www.ogd.stadt-zuerich.ch/wfs/geoportal/Zueri_wie_neu?service=WFS&version=1.1.0&request=GetFeature&outputFormat=GeoJSON&typename=zwn_meldungen_p|