import json
import os

CANT_BE_MORE = 9.0 * 10**9


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


def get_biggest_bar(data: list) -> list:
    result = max(data, key=seats)
    return name(result)


def get_smallest_bar(data: list) -> list:
    result = min(data, key=seats)
    return name(result)


def get_closest_bar(data: list, longitude: str, latitude: str) -> list:
    min_distance = CANT_BE_MORE
    result = []

    def find_distance(x1, y1, x2, y2):
        from math import sqrt
        return sqrt((x2-x1)**2 + (y2-y1)**2)

    for bar in data:
        bar_coordinates = coordinates(bar)
        distance = find_distance(bar_coordinates[0], bar_coordinates[1], float(longitude), float(latitude))
        if distance < min_distance:
            min_distance = distance
            result.clear()
            result.append(name(bar))
        elif distance == min_distance:
            result.append(name(bar))
    return result


if __name__ == '__main__':
    path = input('Input a path to your JSON file: ')
    data_to_use = load_data(path)
    if not data_to_use:
        print("File not found.\n")
    else:
        print("The biggest bar(-s): {}\n".format(get_biggest_bar(data_to_use)))
        print("The smallest bar(-s): {}\n".format(get_smallest_bar(data_to_use)))
        while True:
            your_longitude = input("Input your longitude: ")
            if not your_longitude:
                break
            your_latitude = input("Input your latitude: ")
            if not your_latitude:
                break
            print("The closest bar(-s): {}\n".format(get_closest_bar(data_to_use, your_longitude, your_latitude)))
