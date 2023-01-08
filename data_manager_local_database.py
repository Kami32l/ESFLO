import pandas as pd


class DatabaseManager:
    """
    This class is responsible for reading from and writing to the database file with info about user and their flights.
    """

    def __init__(self):
        self.file_name = 'database.csv'
        self.read_file()

    def read_file(self):
        """
        Reads from the database.
        :return file: data from the database
        """

        try:
            self.file = pd.read_csv(self.file_name, delimiter=';')
        except FileNotFoundError:
            self.file = self.create_file()
            self.save_data_to_file()

    def save_data_to_file(self):
        """
        Writes the pandas frame to the database file.
        """
        self.file.to_csv(self.file_name, sep=';', decimal=',', index=False)

    def update_file(self, email, password, city, iata, maxprice, dep_city, dep_iata, people, days_range, next_date):
        """
        Adds user data to the pandas frame.
        :param email: email address ("email@gmail.com")
        :param password: password already hashed ("pssstisas3cr3tphras3")
        :param city: airport city name ("Paris")
        :param iata: airport IATA code ("PAR")
        :param maxprice: maximum price you want to spend on flight, for example: 25
        :param dep_city: departure airport city name ("Poznan")
        :param dep_iata: departure airport IATA code ("POZ")
        :param people: number of adults
        :param days_range: number of days to search in
        :param next_date: end date of searching
        """
        frame = {'Email': email, 'Password': password, 'City': city, 'IATA': iata, 'MaxPrice': maxprice,
                 'Dep_city': dep_city, 'Dep_IATA': dep_iata, 'People': people,
                 'Days_range': days_range, 'Next_date': next_date}
        # self.file.append(frame, ignore_index=True)

        self.file = pd.concat([self.file, pd.DataFrame.from_records([frame])])

    def search_database(self, key, word, key2, word2):
        """
        Searches database for a record. Two set of a key and a word. If key == word returns all rows matching
        from DataFrame.
        :param key: column name ('email')
        :param key2: column name ('password')
        :param word: what to look for in the column ('email@gmail.com')
        :param word2: what to look for in the column ('password')
        :return: all rows matching from the database
        """

        # This line of code will return all
        # rows which satisfies both the conditions
        # ie value of age == 35 and value of age == 40

        return self.file[(self.file[f"{key}"] == f'{word}') & (self.file[f"{key2}"] == f'{word2}')]

    def search_database_one(self, key, word):
        """
        Searches database for a record. One key and one word. If key == word returns all rows matching from DataFrame.
        :param key: column name ('email')
        :param word: what to look for in the column ('email@gmail.com')
        :return: all rows matching from the database
        """

        return self.file.loc[self.file[f"{key}"] == f'{word}']

    def create_file(self):
        new_file = pd.DataFrame(columns=['Email', 'Password', 'City', 'IATA', 'MaxPrice', 'Dep_city', 'Dep_IATA',
                                         'People', 'Days_range', 'Next_date'])
        return new_file
