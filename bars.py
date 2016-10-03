import json


def load_data(filepath: str) -> list:
    import os
    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding='utf-8') as handle:
        return json.JSONDecoder().decode(handle)


def name(bar: dict) -> str:
    return bar['Cells']['Name']


def seats(bar: dict) -> int:
    return bar['Cells']['SeatsCount']


def coordinates(bar: dict) -> list:
    return bar['Cells']['goeData']['coordinates']


def get_biggest_bar(data: list) -> list:
    max_seats = 0
    result = []
    for bar in data:
        if seats(bar) > max_seats:
            max_seats = seats(bar)
            result.clear()
            result.append(name(bar))
        elif seats(bar) == max_seats:
            result.append(name(bar))
    return result


def get_smallest_bar(data: list) -> list:
    min_seats = 9 * 10**10
    result = []
    for bar in data:
        if seats(bar) < min_seats:
            min_seats = seats(bar)
            result.clear()
            result.append(name(bar))
        elif seats(bar) == min_seats:
            result.append(name(bar))
    return result


def get_closest_bar(data: list, longitude: float, latitude: float) -> list:
    min_distance = 9 * 10**10
    result = []

    def find_distance(x1, x2, y1, y2):
        from math import sqrt
        return sqrt((x2-x1)**2 + (y2-y1)**2)

    for bar in data:
        bar_coordinates = coordinates(bar)
        distance = find_distance(bar_coordinates[0], bar_coordinates[1], longitude, latitude)
        if distance < min_distance:
            min_distance = distance
            result.clear()
            result.append(name(bar))
        elif distance == min_distance:
            result.append(name(bar))
    return result


if __name__ == '__main__':
    pass
