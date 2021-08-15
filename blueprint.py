from math import cos, asin, sqrt, pi

import requests
from flask import request, Blueprint, render_template

blueprint = Blueprint("blueprint", __name__,
                      static_folder="static", template_folder="template")


def getDistance(latitude, longitude):
    '''
    Uses the haversine formula by the link;
    https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula
    In addition, the following links were used for MKAD location details. Radius, center coordinates etc.
    https://en.wikipedia.org/wiki/Moscow_Ring_Road
    https://en.wikipedia.org/wiki/Module:Location_map/data/Russia_Moscow_MKAD
    '''
    mkad_latitude = 55.71
    mkad_longitude = 37.61
    p = pi / 180
    a = 0.5 - cos((mkad_latitude - latitude) * p) / 2 + cos(latitude * p) * \
        cos(mkad_latitude * p) * (1 - cos((mkad_longitude - longitude) * p)) / 2
    d = 12742 * asin(sqrt(a))
    return d - 54,45


def getCoordinates(add=None):
    '''
    Api response details are below;
    https://yandex.ru/dev/maps/geocoder/doc/desc/reference/response_structure.html
    '''
    API_KEY = "8da02334-bb40-438b-9fec-8c2fcecfc1ea"
    location = add if add is not None else request.form['address']
    r = requests.get("https://geocode-maps.yandex.ru/1.x/?format=json&apikey=" +
                     API_KEY + "&lang=en_US&geocode=" + location)
    json_object = r.json()
    try:
        coords = json_object['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
        return float(coords[1]), float(coords[0])
    except:
        ValueError


@blueprint.route("/mkad", methods=['POST'])
def distance_calculator():
    latitude, longitude = getCoordinates()
    distance = getDistance(latitude, longitude)
    if distance <= 0:
        return render_template("mkad.html")
    else:
        return render_template("distance.html", distance=distance)


@blueprint.route("/")
def home():
    return render_template("index.html")
