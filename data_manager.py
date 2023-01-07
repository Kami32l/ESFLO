import requests
import os
from dotenv import load_dotenv

load_dotenv("C:\\Users\\T430\\python\\EnvironmentVariables\\.env")
SHEETY_CO_AUTHORIZATION = os.getenv("SHEETY_CO_AUTHORIZATION2")
SHEETY_CO_SHEET_ENDPOINT = os.getenv("SHEETY_CO_SHEET_ENDPOINT")


class DataManager:
    """
    This class is responsible for talking to the Google Sheet using SHEETY.CO API.
    """
    def __init__(self):
        pass

    def get_data(self):
        """
        Gets data from Google Sheet.
        :return:
        """
        headers = {
            "Authorization": SHEETY_CO_AUTHORIZATION
        }
        endpoint = SHEETY_CO_SHEET_ENDPOINT
        r = requests.get(url=endpoint, headers=headers)
        data = r.json()
        print(data)
        return data

    def add_row(self, user, city, iata_code, lowest_price):
        """
        Append row to a Google spreadsheet.
        :param user: username ("John Travolta")
        :param city: airport city name ("Paris")
        :param iata_code: airport IATA code ("PAR")
        :param lowest_price: maximum price you want to spend on flight, for example: 25
        """
        headers = {
            "Authorization": SHEETY_CO_AUTHORIZATION,
        }
        parameters = {
            "price": {
                "user": user,
                "city": city,
                "iata": iata_code,
                "price": lowest_price,
            }
        }
        endpoint = SHEETY_CO_SHEET_ENDPOINT
        r = requests.post(url=endpoint, json=parameters, headers=headers)
        # print(r.text)
        # print(r.url)
