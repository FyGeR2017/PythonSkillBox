import requests
import json

def get_millennium_falcon_info():
    url = 'https://swapi.dev/api/starships/?search=Millennium Falcon'
    response = requests.get(url)
    data = response.json()
    
    if data['count'] > 0:
        ship_info = data['results'][0]
        
        # Получаем информацию о судне
        name = ship_info['name']
        max_speed = ship_info['max_atmosphering_speed']
        starship_class = ship_info['starship_class']
        pilots_urls = ship_info['pilots']
        
        pilots_info = []
        
        # Получаем информацию о пилоте
        for pilot_url in pilots_urls:
            pilot_response = requests.get(pilot_url)
            pilot_data = pilot_response.json()
            
            pilot_name = pilot_data['name']
            pilot_height = pilot_data['height']
            pilot_mass = pilot_data['mass']
            pilot_homeworld = pilot_data['homeworld']
            pilot_homeworld_url = pilot_data['homeworld']
            
            # Получаем родную планету
            homeworld_response = requests.get(pilot_homeworld_url)
            homeworld_data = homeworld_response.json()
            pilot_homeworld_name = homeworld_data['name']
            
            pilot_info = {
                'name': pilot_name,
                'height': pilot_height,
                'mass': pilot_mass,
                'homeworld': pilot_homeworld_name,
                'homeworld_url': pilot_homeworld
            }
            
            pilots_info.append(pilot_info)
        
        ship_info = {
            'name': name,
            'max_speed': max_speed,
            'class': starship_class,
            'pilots': pilots_info
        }
        
        return ship_info
    else:
        return None

# Получаем информацию по Millennium Falcon
millennium_falcon_info = get_millennium_falcon_info()

# Выводим информацию в консоль
if millennium_falcon_info:
    print(json.dumps(millennium_falcon_info, indent=4))
else:
    print("Millennium Falcon not found!")
