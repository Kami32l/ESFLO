# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from date_data import DateData
# from notification_manager import NotificationManager
from data_manager_local_database import DatabaseManager
from password_hashing import hash_password
from gui import GUI
import os
from dotenv import load_dotenv

load_dotenv("C:\\Users\\T430\\python\\EnvironmentVariables\\.env")
CITY_FLY_FROM_IATA = os.getenv("CITY_FLY_FROM_IATA")

#TODO replace user first name, last name with email and password (maybe later hashed?)
#TODO error handling
#TODO Error display message box with tkinter


def add_city():
    """
    Asks user for city. Gets IATA code for the city using class using kiwi API.
    """

    city = input("City: ")
    price = input("Lowest price: ")
    iata = FlightSearch().get_location_code(city)
    d = DataManager()
    d.add_row(city, iata, price)

        #TODO ASKING USER FOR DATA <?>
        #TODO USER GRAPHICAL INTERFACE


def main():
    """
    Main function.
    """

    # d = DateData(30)   # TODO max range 1-365 days  #ok
    # today_date = d.today_date
    # next_date = d.next_date
    # print(today_date, next_date)

    #data = DataManager().get_data()
    # test data
    # data = {'prices': [{'city': 'Paris', 'iata': 'PAR', 'price': 30, 'id': 2}, {'city': 'Barcelona', 'iata': 'BAR',
    # 'price': 80, 'id': 3}, {'city': 'Athens', 'iata': 'ATH', 'price': 50, 'id': 4}, {'city': 'Rome', 'iata': 'ROM',
    # 'price': 50, 'id': 5}, {'city': 'Istanbul', 'iata': 'IST', 'price': 90, 'id': 6}]}

    # dbM = DatabaseManager()

    #start GUI
    gui = GUI()
    print(gui.user_email)
    print(gui.user_password)

    # dbM.update_file(user="Kacper Boczniak", city="Paris", iata="PAR", maxprice=35)  # TODO Search czy record istnieje
    # dbM.save_data_to_file()

    # print(dbM.file)
    # filtered_result = dbM.file.loc[dbM.file['Email'] == 'julio.donder@gmail.com'] #searches database
    # print(filtered_result)    #TODO Return data connected to a name


    #iterates through name filtered data
    # number_of_adults = 1
    #
    # # clear the file before writing to it
    # file = open("results.txt", "w")
    # file.write("")
    # file.close()
    #
    # for index, row in filtered_result.iterrows():
    #     # print(row)
    #     # print(row["User"], row["MaxPrice"])
    #
    #     city = row['City']
    #     fly_to = row['IATA']
    #     fly_from = CITY_FLY_FROM_IATA
    #     date_from = today_date
    #     date_to = next_date
    #     # print("Next_date:", next_date)
    #     price_to = row['MaxPrice']
    #     adults = number_of_adults
    #
    #     #checks flights
    #     results = FlightSearch().check_flights(fly_from=fly_from, fly_to=fly_to, date_from=date_from, date_to=date_to,
    #                                            price_to=price_to, adults=adults)
    #     # print("Results:", results)
    #
    #     #formats received found flights data
    #     formated_data = FlightData().format_data(results, city)
    #     for elem in formated_data:
    #         # print("Elem:", elem)
    #         # NotificationManager().send_sms(elem)  //sends sms message
    #         elem_to_write = "\n\n" + elem
    #         file = open("results.txt", "a")
    #         file.write(elem_to_write)
    #         file.close()


# add_city()
main()
