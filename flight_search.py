import requests
import os
from dotenv import load_dotenv

load_dotenv("C:\\Users\\T430\\python\\EnvironmentVariables\\.env")
KIWI_API_KEY = os.getenv("KIWI_API_KEY")


class FlightSearch:
    """
    This class is responsible for talking to the Kiwi Flight Search API.
    documentation - https://tequila.kiwi.com/docs/tequila_api/search_api
    """
    def __init__(self):
        pass

    def get_location_code(self, city_name):
        """
        Gets IATA code for the specified city using Twillio API
        :param city_name: city name
        :return: city iata code
        """
        headers = {
            "apikey": KIWI_API_KEY,
        }
        parameters = {
            "term": city_name,
            "locale": "en-EN",
            "location_types": "city",
        }
        endpoint = "https://tequila-api.kiwi.com/locations/query"
        code = 0
        try:
            r = requests.get(url=endpoint, params=parameters, headers=headers)
            # print("status code get_location_code:", r.status_code)
            data = r.json()
            # print(r.url)
            # print(data)
            status = 1
            try:
                code = data['locations'][0]['code']
            except IndexError:
                code = 0
        except requests.exceptions.ConnectionError:
            # TODO no connection window
            # print("no internet connection")
            status = 0

        # print(code)
        return code, status

    def check_flights(self, fly_from, fly_to, date_from, date_to, price_to, adults=1, max_stopovers=3,
                      max_fly_duration=18, **kwargs):
        """
        Checks for available flights using Kiwi.
        :param fly_from: city's of the departure IATA code
        :param fly_to: city's of the arrival IATA code
        :param date_from: starting date to look for a flight
        :param date_to: ending date to look for a flight
        :param price_to: maximal price
        :param adults: number of adults on the flight
        :param max_stopovers: maximal number of stops/changing the flights during travel to destination
        :param max_fly_duration: maximal duration of the flight (in hours)
        :param kwargs: Kiwi flight API provides more parameters than this method has specified more info in Kiwi Docs.
        :return: available flights
        """

        headers = {
            "apikey": KIWI_API_KEY,
        }
        parameters = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "price_to": price_to,
            "sort": "price",    # quality, price, date or duration.
            "vehicle_type": "aircraft",
            "limit": 1,
            "adults": adults,
            "max_stopovers": max_stopovers,
            "max_fly_duration": max_fly_duration,
        }

        # print(kwargs.items())
        for key, value in kwargs.items():
            parameters[key] = value

        endpoint = "https://tequila-api.kiwi.com/v2/search"

        try:
            r = requests.get(url=endpoint, params=parameters, headers=headers)
            data = r.json()
            status = 1
        except requests.exceptions.ConnectionError:
            # TODO no connection window
            # print("no internet connection")
            data = []
            status = 0

        # print(r.url)
        # print(data)
        return data, status
