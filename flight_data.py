from flight_search import FlightSearch
from date_data import DateData


class FlightData:
    """
    This class is responsible for structuring the flight data.
    """

    def __init__(self):
        pass

    def format_data(self, results):
        """
        Filters received data to only specified contents
        :param results: data to be filtered and formatted
        :return formatted_data: formatted messages in a list
        :return link: flight links list
        """
        formatted_data = []
        links = []

        for result in results['data']:

            city = result['cityTo']
            dep_city = result['cityFrom']
            price = result['price']
            departure = result['utc_departure'] + " UCT"
            arrival = result['utc_arrival']
            distance = result['distance']
            stops_count = int(result['pnr_count'])-1
            seats = result['availability']['seats']
            link = result['deep_link']

            # print(result)
            # message = print(f"Flight for {city}")
            #             print("Price: ", price, "€")
            #             print("Departure: ", departure)
            #             print("Arrival: ", arrival)
            #             print("Distance: ", distance, "km")
            #             print("Route stops: ", stops_count)
            #             print("Seat availability: ", seats)
            #             print("Link: ", link)

            message_text = self.format_message(city, dep_city, price, departure, arrival, distance, stops_count, seats, link)

            formatted_data.append(message_text)
            links.append(link)

        try:
            return formatted_data, links
        except IndexError:
            formatted_data = "Flight not found"
            links = "Link for flight not found"
            return formatted_data, links

    def format_message(self, city, dep_city, price, departure, arrival, distance, stops_count, seats, link):
        """
        Formats received data into string text message.
        :param city: city of arrival
        :param dep_city: city of departure
        :param price: max price
        :param departure: departure time
        :param arrival: arrival time
        :param distance: distance of travel
        :param stops_count: number of times you need to change a plane
        :param seats: number of seats available
        :param link: link to an offer
        :return: message text
        """
        message_text = f"Lot do {city} z {dep_city}\nCena: {price}€\n" \
                       f"Odlot: {departure}\nPrzylot: {arrival}\n" \
                       f"Dystans: {distance}km\nMiędzylądowania: {stops_count}\n" \
                       f"Dostępność miejsc: {seats}\n" \
                       # f"Link: {link}"

        # f"Flight for {city}, Price: {price}€\n" \
        # f"Departure: {departure}, Arrival: {arrival}\n" \
        # f"Distance: {distance}km, Stops: {stops_count}\n" \
        # f"Seat availability: {seats}\n" \
        # f"Link: {link}"
        return message_text

    def filter_from_database(self, to_filter):
        """
        Prepare data to flight search and search for a flight.
        :param to_filter: data to filter
        :return results:
        """

        # iterates through filtered data
        status_code = 1
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
            found_flight, status_code = FlightSearch().check_flights(fly_from=fly_from, fly_to=fly_to, date_from=date_from,
                                                        date_to=date_to, price_to=price_to, adults=adults)
            if status_code == 0:
                return results, status_code

            results.append(found_flight)

        print("Results loc flight_data.py filter_from_database():", results)
        return results, status_code

    def filter_from_user_input(self, city, fly_to, fly_from, days_range, price_to, adults):
        """
        Prepare data to the flight search and search for a flight.
        :param city: city of arrival
        :param fly_to: iata code city of arrival
        :param fly_from: iata code cifty of departure
        :param days_range: days to search flights in counted from today
        :param price_to: max price
        :param adults: number of adults
        :return: found flight
        """

        d = DateData(int(days_range))
        date_from = d.today_date
        date_to = d.next_date
        # print("Next_date:", next_date)

        # checks flights
        found_flight, status_code = FlightSearch().check_flights(fly_from=fly_from, fly_to=fly_to, date_from=date_from,
                                                    date_to=date_to, price_to=price_to, adults=adults)

        print("Results loc flight_data.py filter_from_user_input():", found_flight)
        return found_flight, status_code
