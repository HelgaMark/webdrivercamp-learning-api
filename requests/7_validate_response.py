import json
import requests
from pprint import pprint


def find_mismatched_data(url, file_name):
    response = requests.get(url)
    actual_data = response.json()['results']

    with open(file_name, 'r') as file:
        expected_data = json.load(file)['results']

    mismatches = {}

    for actual_planet, expected_planet in zip(actual_data, expected_data):
        planet_name = actual_planet['name']
        planet_mismatches = {}

        for key in expected_planet:
            if actual_planet[key] != expected_planet[key]:
                planet_mismatches[key] = {
                    'Expected': expected_planet[key],
                    'Actual': actual_planet[key]
                }

    if planet_mismatches:
        mismatches[planet_name] = planet_mismatches

    return mismatches


if __name__ == "__main__":
    url = "https://swapi.dev/api/planets/"
    file_name = "planets.json"

    pprint(find_mismatched_data(url, file_name))
