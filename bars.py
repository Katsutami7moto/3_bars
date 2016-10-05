import json
import os
from math import sqrt
import sys


def load_data(filepath: str) -> list:
    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding='utf-8') as handle:
        return json.load(handle)


def name(bar: dict) -> str:
    return bar['Cells']['Name']


def seats(bar: dict) -> int:
    return bar['Cells']['SeatsCount']


def coordinates(bar: dict) -> tuple:
    return bar['Cells']['geoData']['coordinates'][0], bar['Cells']['geoData']['coordinates'][1]


def get_biggest_bar(data: list) -> str:
    result = max(data, key=seats)
    return name(result)


def get_smallest_bar(data: list) -> str:
    result = min(data, key=seats)
    return name(result)


def get_closest_bar(data: list, longitude: str, latitude: str) -> str:

    def find_distance(bar: dict) -> float:
        x1, y1 = coordinates(bar)
        return sqrt((float(longitude)-x1)**2 + (float(latitude)-y1)**2)

    result = min(data, key=find_distance)
    return name(result)


if __name__ == '__main__':
    path = input('Input a path to your JSON file: ')
    data_to_use = load_data(path)
    if not data_to_use:
        print('File not found.\n')
        sys.exit(1)

    print('The biggest bar(-s): "{}"\n'.format(get_biggest_bar(data_to_use)))
    print('The smallest bar(-s): "{}"\n'.format(get_smallest_bar(data_to_use)))

    while True:
        your_longitude = input('Input your longitude: ')
        if not your_longitude:
            break
        your_latitude = input('Input your latitude: ')
        if not your_latitude:
            break
        print('The closest bar(-s): "{}"\n'.format(get_closest_bar(data_to_use, your_longitude, your_latitude)))
