from geopy.geocoders import Nominatim
import time
import pandas as pd

geolocator = Nominatim(user_agent = 'geopyExercises')
#data = pd.read_csv('datasets/kc_house_data.csv')

#Criar uma coluna com lat e long concatenados por ,
data['query'] = data[['lat', 'long']].apply(lambda x: str(x['lat']) + ',' + str(x['long']), axis = 1) #axis = 1, porque o concat é linha a linha, já que temos 2 colunas no apply

def get_data (x):
    index, row = x
    time.sleep(0.5)

    response = geolocator.reverse(query)

    place_id = response.raw['place_id']
    osm_type = response.raw['osm_type']
    country = response.raw['adress']['country']
    country_code = response.raw['adress']['country_code']

    return place_id,osm_type, country, country_code