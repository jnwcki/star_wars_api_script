import requests


people_url = "http://swapi.co/api/people"
films_url = "http://swapi.co/api/films"
vehicles_url = "http://swapi.co/api/vehicles"


def get_data(url):
    urlresponse = requests.get(url).json()
    return urlresponse


def get_results(key, url):
    urlresponse = requests.get(url).json()
    response = urlresponse.get('results')
    return response


def person_search():
    key = input("Search for person: ")
    for person in get_results(key, people_url):
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


def film_search():
    key = input('Enter film title: ')
    for film in get_results(key, films_url):
        if film.get('title').lower() == key.lower():
            print('\nTitle: ' + film['title'])
            print('Episode ID: ' + str(film['episode_id']))
            print('Opening Crawl: \n' + film['opening_crawl'])
            print('Director: ' + film['director'])
            print('Producer: ' + film['producer'])
            print('Release Date: ' + film['release_date'])
            print('\nTop 3 Actors:')
            for actor in film['characters'][:3]:
                print(get_data(actor)['name'])


def vehicle_search():
    key = input('Enter Vehicle Name: ')
    for vehicle in get_results(key, vehicles_url):
        if vehicle.get('name').lower() == key.lower():
            print('Name: ' + vehicle['name'])
            print('Model: ' + vehicle['model'])
            print('Manufacturer: ' + vehicle['manufacturer'])
            print('Cost in credits: ' + str(vehicle['cost_in_credits']))
            print('Length: ' + str(vehicle['length']))
            print('Max Atmosphering Speed: ' + str(vehicle['max_atmosphering_speed']))
            print('Crew: ' + str(vehicle['crew']))
            print('Passengers: ' + str(vehicle['passengers']))
            print('Cargo Capacity: ' + str(vehicle['cargo_capacity']))
            print('Consumables: ' + vehicle['consumables'])
            print('Vehicle Class: ' + vehicle['vehicle_class'])

            print('\nPilots:')
            for vehicle_pilot in vehicle['pilots']:
                print(get_data(vehicle_pilot)['name'])

            print('\nFilms:')
            for vehicle_film in vehicle['films']:
                print(get_data(vehicle_film)['title'])


def list_items(url):
    next = get_data(url).get('next')
    for critter in get_data(url).get('results'):
        print(critter.get('name'))
    if get_data(next) != 'null':
        if input("\nEnter for next page, q to quit: ").lower() != 'q':
            list_items(next)

while True:
    print("\nWelcome to the Star Wars API Explorer\n")
    welcome_input = input("Enter (C) for a list of characters, (F) for a list of films or \n(V) for a list of "
                          "vehicles. (D) for detail menu: ").lower()
    if welcome_input == 'c':
        list_items(people_url)

    elif welcome_input == 'f':
        for film in get_data(films_url).get('results'):
            print(film.get('title'))

    elif welcome_input == 'v':
        list_items(vehicles_url)

    elif welcome_input == 'd':
        detail_input = input("\nSearch details of (C) characters, (F) Films or (V) Vehicles: ").lower()

        if detail_input == 'c':
            person_search()

        elif detail_input == 'f':
            film_search()

        elif detail_input == 'v':
            vehicle_search()
