from geopy.geocoders import Nominatim # Módulo de manipulazação de dados de geolocalização

geolocalizacao = Nominatim(user_agent='Geolocalizacao') # Nomeia o usuário

lista = str(geolocalizacao.geocode('New York')).split(',') # Retorna o endereço completo de parte de um endereço

for i in lista:
    print(i)