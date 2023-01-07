import pandas as pd


class DatabaseManager:
    """
    This class is responsible for reading from and writing to database file with info about flights.
    """

    def __init__(self):
        self.file = self.read_file()
        pass

    def read_file(self):
        """
        Reads from the database.
        :return file: data from the database
        """

        file = pd.read_csv('database.txt', delimiter=';')
        # print(file)

        return file

    def save_data_to_file(self):
        """
        Writes the pandas frame to the database file.
        """
        self.file.to_csv('database.txt', sep=';', decimal=',', index=False)

    def update_file(self, email, password, city, iata, maxprice, dep_city, dep_iata, people, days_range, next_date):
        """
        Adds user data to the pandas frame.
        :param email: email address ("email@gmail.com")
        :param password: password ("pssstisas3cr3tphras3")
        :param city: airport city name ("Paris")
        :param iata: airport IATA code ("PAR")
        :param maxprice: maximum price you want to spend on flight, for example: 25
        :param dep_city: departure airport city name ("Poznan")
        :param dep_iata: departure airport IATA code ("POZ")
        :param people: number of adults
        :param days_range: number of days to search in
        :param next_date: end date of searching
        """
        frame = {'Email': email, 'Password': password, 'City': city, 'IATA': iata, 'MaxPrice': maxprice, 'Dep_city': dep_city,
                 'Dep_IATA': dep_iata, 'People': people, 'Days_range': days_range, 'Next_date': next_date}
        # self.file.append(frame, ignore_index=True)

        self.file = pd.concat([self.file, pd.DataFrame.from_records([frame])])

    def search_database(self, key, word):
        """
        Searches database for a record.
        :param key: column name ('email')
        :param word: what to look for in the column ('email@gmail.com')
        :return: all data for the record from the database
        """
        return self.file.loc[self.file[f'{key}'] == f'{word}']

