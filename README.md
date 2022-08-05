# Sao Paulo Housing Prices

Sao Paulo is the 8th most populous city on Earth and its metropolitan region, with over 30 million inhabitants, one of the largest urban agglomerations in the world. Its real estate market is a critical part of the economy and it has a huge impact on many aspects of life. In this notebook, you will find a comprehensive analysis of the residential properties for sale accross different neighborhoods. The purpose is to look for insights in the data and identify the key aspects that define housing prices in this geographic context.

## Content

- [1 - Preparing and cleaning up data](sp-housing-clean.ipynb)
- [2 - Geolocating properties](sp-housing-geo.ipynb)
- [3 - Exploring property types](sp-housing-properties.ipynb)
- [4 - Housing types and prices](sp-housing-prices.ipynb)
- [5 - Housing types per location](sp-housing-geospattypes.ipynb)
- [6 - Housing prices per location](sp-housing-geospatprices.ipynb)
- [7 - Relation between housing types and demographics](sp-housing-demorelat.ipynb)
- [8 - Price predicting model](sp-housing-pricepredict.ipynb)

## Links to Original 
Let's take a look at the source data, which consists of four dataframes:

### [Sao_Paulo.csv](https://www.kaggle.com/datasets/kaggleshashankk/house-price-data-of-sao-paulo/download?datasetVersionNumber=1)
Contains a number of residential properties listed for sale in the city of Sao Paulo.

### [sp_addresses.csv](https://drive.google.com/file/d/1msFHO93b6Vncna1RW1389Ovlmky_VZHD/view?usp=sharing)
Contains a complete list of addresses, postcodes, latitudes and longitudes in the city of Sao Paulo.
### [Basico_SP1.csv](https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html)
Contains census demographic data of Sao Paulo published by the Brazilian Institute of Geography and Statistics (IBGE), in 2010.

Tree to file: Censo_Demografico_2010 > Resultados_do_Universo > Agregados_por_Setores_Censitarios > SP_Capital_20190207.zip > Base > CSV > Basico_SP1.csv

### [SP_Setores_2020.shp](https://www.ibge.gov.br/geociencias/downloads-geociencias.html?caminho=organizacao_do_territorio/malhas_territoriais/malhas_de_setores_censitarios__divisoes_intramunicipais/2020/Malha_de_setores_(shp)_por_UFs)
Contains geospatial polygons that identify the sectors investigated by the Brazilian Institute of Geography and Statistics (IBGE), in 2010.

Source file: SP_Setores_2020.zip

## Setup

`pip freeze > requirements.txt`

`python3 -m venv venv`

`pip install -r requirements.txt`

`pip install ipykernel`
