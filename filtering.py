from flight_search import FlightSearch
from date_data import DateData


class PrepareDataToSearch:
    """

    """

    def __init__(self):
        pass

    def filter_from_database(self, to_filter):
        # iterates through name filtered data
        number_of_adults = 1

        results = []
        for index, row in to_filter.iterrows():
            # print(row)
            # print(row["User"], row["MaxPrice"])


            city = row['City']
            fly_to = row['IATA']
            fly_from = row['Dep_IATA']

            d = DateData(row['Days_range'])
            date_from = d.today_date

            date_to = row['Next_date']
            # print("Next_date:", next_date)
            price_to = row['MaxPrice']
            adults = row['People']

            # checks flights
            found_flight = FlightSearch().check_flights(fly_from=fly_from, fly_to=fly_to, date_from=date_from,
                                                        date_to=date_to, price_to=price_to, adults=adults)
            results.append(found_flight)

        print("Results (filtering):", results)
        return results

    def filter_from_user_input(self, city, fly_to, fly_from, days_range, price_to, adults):

        d = DateData(int(days_range))
        date_from = d.today_date
        date_to = d.next_date
        # print("Next_date:", next_date)

        # checks flights
        found_flight = FlightSearch().check_flights(fly_from=fly_from, fly_to=fly_to, date_from=date_from,
                                                    date_to=date_to, price_to=price_to, adults=adults)

        print("Results (filtering):", found_flight)
        return found_flight
