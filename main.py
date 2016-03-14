import requests


people_url = "http://swapi.co/api/people"
films_url = "http://swapi.co/api/films"
vehicles_url = "http://swapi.co/api/vehicles"


def get_data(url):
    urlresponse = requests.get(url).json()
    return urlresponse


def get_person(key, url):
    urlresponse = requests.get(url).json()
    response = urlresponse.get('results')
    return response


def person_search():
    key = input("Search for person: ")
    for person in get_person(key, people_url):
        if person.get('name').lower() == key.lower():
            print('Name: ' + person['name'])
            print('Height: ' + person['height'])
            print('Mass: ' + person['mass'])
            print('Hair Color: ' + person['hair_color'])
            print('Skin Color: ' + person['skin_color'])
            print('Eye Color: ' + person['eye_color'])
            print('Birth Year: ' + person['birth_year'])
            print('Gender: ' + person['gender'])
            print('Homeworld: ' + person['homeworld'])
            print('\nFilms: ')
            for film in person['films']:
                print(get_data(film)['title'])
            print('\nSpecies: ')
            for critter in person['species']:
                print(get_data(critter)['name'])
            print('\nVehicles: ')
            for vehicle in person['vehicles']:
                print(get_data(vehicle)['name'])
            print('\nStarships:')
            for ship in person['starships']:
                print(get_data(ship)['name'])


while True:
    print("\nWelcome to the Star Wars API Explorer\n")
    welcome_input = input("Enter (C) for a list of characters, (F) for a list of films or \n(V) for a list of "
                          "vehicles. (D) for detail menu.").lower()
    if welcome_input == 'c':
        for critter in get_data(people_url).get('results'):
            print(critter.get('name'))
    elif welcome_input == 'f':
        for film in get_data(films_url).get('results'):
            print(film.get('title'))
    elif welcome_input == 'v':
        for ride in get_data(vehicles_url).get('results'):
            print(ride.get('name'))

    elif welcome_input == 'd':
        detail_input = input("Search details of (C) characters, (F) Films or (V) Vehicles").lower()

        if detail_input == 'c':
            person_search()
