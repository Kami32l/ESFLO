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

        :return formated_data: returns formatted data
        :return link: returns link
        """
        formatted_data = []
        links = []

        for result in results['data']:
            try:
                city = result['cityTo']
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

                message_text = self.format_message(city, price, departure, arrival, distance, stops_count, seats, link)

                formatted_data.append(message_text)
                links.append(link)

            except IndexError:
                print(f"No flights for {city}")

        print("formated_data", formatted_data)

        try:
            return formatted_data, links
        except IndexError:
            formatted_data = "Flight not found"
            links = "Link for flight not found"
            return formatted_data, links

    def format_message(self, city, price, departure, arrival, distance, stops_count, seats, link):
        """
        Formats received data into string text message used for SMS notification (Twilio API)
        :param city:
        :param price:
        :param departure:
        :param arrival:
        :param distance:
        :param stops_count:
        :param seats:
        :param link:
        :return:
        """
        message_text = f"Lot do {city}\nCena: {price}€\n" \
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
