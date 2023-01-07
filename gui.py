# do zrobienia
# na gorze stronu zawsze dostepne przechodzenie miedzy menu
# 0. TODO I. Menu wyboru wyszukanie (+ funkcja zapisu do usera)/II. logowanie user - odczyt
# 1. TODO II. Wyszukaj lot wedlug zapisanych danych
# 2. TODO II. Wpisywanie danych lotu
# 2. TODO Zapisz kryteria lotu uzytkownika
# 3. TODO Pokaz dane lotu
#    TODO SET BACKGROUND IMAGE

from tkinter import *
from password_hashing import hash_password
from data_manager_local_database import DatabaseManager
from tkinter import messagebox
from filtering import PrepareDataToSearch
from flight_data import FlightData
from scrollable_frame import ScrollbarFrame
from flight_search import FlightSearch
from date_data import DateData

THEME_COLOR = "#00CD33"


class GUI:

    def __init__(self):
        self.user_email = ""
        self.user_password = ""

        self.main_window()

    def main_window(self):
        """
        Generates main window.
        :return:
        """

        WINDOW_WIDTH = 600
        WINDOW_HEIGHT = 300

        ws = Tk()
        ws.title("Flight Deals Search Tool - Main Menu")

        # get the screen dimension
        screen_width = ws.winfo_screenwidth()
        screen_height = ws.winfo_screenheight()

        # find the center point
        center_x = int(screen_width / 2 - WINDOW_WIDTH / 2)
        center_y = int(screen_height / 2 - WINDOW_HEIGHT / 2)

        # set the position of the window to the center of the screen
        ws.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{center_x}+{center_y}')

        # set background color
        ws.config(bg="#00CD33")

        # functions
        def login():
            # login function checks email and password
            email_check = email.get()
            password_check = password.get()

            check_count = 0

            # checks if provided email field not empty if it is show warning
            if email_check == "":
                warn = "Email can't be empty!"
                messagebox.showwarning("Warning", warn)
            else:
                check_count += 1
                self.user_email = email_check

            # checks if password field empty, if not hashes password
            if password_check == "":
                warn = "Password can't be empty!"
                messagebox.showwarning("Warning", warn)
            else:
                check_count += 1
                self.user_password = hash_password(password_check)

            # when password and email provided are in the database if not = display warning message
            if check_count == 2:
                record_in_database = False
                returned_results = DatabaseManager().search_database('Email', email_check)  # searches database
                print("returned_results", returned_results)
                flights = []
                links = []
                for index, row in returned_results.iterrows():
                    print("index, row", index, row)
                    if row['Password'] == self.user_password and row['Email'] == self.user_email:   # checks if password matches email in the database
                        record_in_database = True

                if record_in_database:
                    print("returned_results", returned_results)
                    results = PrepareDataToSearch().filter_from_database(returned_results)  # znalezione loty raw
                    for i in range(0, len(results)):  # iterates through found flights
                        formatted_data, link = FlightData().format_data(results[i])  # formatowanie danych lotów
                        flights.append(formatted_data)
                        links.append(link)

                    # print(formatted_data)
                    self.flight_show(flights, links)

                else:
                    warn = "Provided credentials incorrect."
                    messagebox.showwarning("Warning", warn)

        # frames
        frame = Frame(ws, padx=20, pady=20, bg="#00CD33")
        frame.pack(expand=False)

        # labels
        Label(frame, text="Menu Główne", bg="#00CD33", fg="#000", font=("Calibri", "24", "bold")).grid(row=0, columnspan=3, pady=10)
        Label(frame, text='Adres Email', bg="#00CD33", fg="#000", font=("Calibri", "14")).grid(row=3, column=0, pady=5)
        Label(frame, text='Hasło', bg="#00CD33", fg="#000", font=("Calibri", "14")).grid(row=4, column=0, pady=5)

        # entry
        email = Entry(frame, width=30)
        password = Entry(frame, width=30)

        email.grid(row=3, column=1)
        password.grid(row=4, column=1)

        # button
        clr = Button(frame, text="WYSZUKAJ LOT\n(BEZ LOGOWANIA)", padx=20, pady=10, relief=SOLID,
                     font=("Calibri", "14", "bold"), command=self.flight_search)

        reg = Button(frame, text="WCZYTAJ LOTY\n(ZALOGUJ)", padx=20, pady=10, relief=SOLID,
                     font=("Calibri", "14", "bold"), command=login)

        ext = Button(frame, text="WYJDŹ", padx=20, pady=21, relief=SOLID,
                     font=("Calibri", "14", "bold"), command=lambda: ws.destroy())

        # button positioning
        clr.grid(row=6, column=0, pady=20)
        reg.grid(row=6, column=1, pady=20)
        ext.grid(row=6, column=2, pady=20)

        ws.mainloop()


    def flight_show(self, data, link):
        """
        Starts window which shows found flights.
        :param data: flight data
        :param link: link for a flight
        """
        WINDOW_WIDTH = 600
        WINDOW_HEIGHT = 600

        ws = Tk()
        ws.title('Flight Deals Search Tool - Flights')
        ws.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')

        # set background color
        ws.config(bg="#00CD33")

        # get the screen dimension
        screen_width = ws.winfo_screenwidth()
        screen_height = ws.winfo_screenheight()

        # find the center point
        center_x = int(screen_width / 2 - WINDOW_WIDTH / 2)
        center_y = int(screen_height / 2 - WINDOW_HEIGHT / 2)

        # set the position of the window to the center of the screen
        ws.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{center_x}+{center_y}')

        # functions

        # frames
        # scrollable frame (for text boxes)
        sbf = ScrollbarFrame(ws)
        ws.grid_rowconfigure(0, weight=1)
        ws.grid_columnconfigure(0, weight=1)
        sbf.configure(background="#00CD33")
        sbf.grid(row=1, column=0, sticky='nsew')
        scrollable_frame = sbf.scrolled_frame

        main_frame_top = Frame(ws, padx=20, pady=0, bg="#00CD33")
        main_frame_top.grid(column=0, row=0)
        # main_frame_top.pack(expand=True)

        label_frame = Frame(main_frame_top, padx=20, pady=0, bg="#00CD33")
        label_frame.grid(column=0, row=0)

        main_frame_bottom = Frame(ws, padx=20, pady=60, bg="#00CD33")
        main_frame_bottom.grid(column=0, row=2)

        buttons_frame = Frame(main_frame_bottom, padx=20, pady=0, bg="#00CD33")
        buttons_frame.grid(column=0, row=0)

        # labels
        Label(label_frame, text="Znalezione loty", bg="#00CD33", fg="#000", font=("Calibri", "24", "bold"))\
            .grid(row=0, columnspan=3)

        # text
        # text boxes which user see, with flight data and links
        row_in_grid = 1
        # iterates through found flights and flight link and put them inside text boxes
        for i in range(0, len(data)):
            row_in_grid += i
            text_box = Text(scrollable_frame, height=7, width=35, background=sbf.scrolled_frame.cget('bg'))
            text_box.grid(column=0, row=row_in_grid)
            try:
                message = data[i][0]
            except IndexError:
                message = "No flights found."
            text_box.insert('end', message)
            text_box['state'] = 'disabled'

            link_box = Text(scrollable_frame, height=7, width=35, background=sbf.scrolled_frame.cget('bg'))
            link_box.grid(column=1, row=row_in_grid)
            # print("LINK(gui)", link[i])
            try:
                message = link[i]
            except IndexError:
                message = "Not found"
            link_box.insert('end', message)
            link_box['state'] = 'disabled'


        # Button
        ext = Button(buttons_frame, text="WYJDŹ", padx=20, pady=10, relief=SOLID, font=("Calibri", "14", "bold"),
                     command=lambda: ws.destroy())
        ext.grid()

        ws.mainloop()


    def flight_search(self):
        """
        Starts window which shows window where you can search for flight.
        :return:
        """

        ws = Tk()
        ws.title('Flight Deals Search Tool - Search Flights')
        ws.geometry('500x400')
        ws.config(bg="#00CD33")
        # ws.attributes('-fullscreen', True)

        WINDOW_WIDTH = 600
        WINDOW_HEIGHT = 600

        # get the screen dimension
        screen_width = ws.winfo_screenwidth()
        screen_height = ws.winfo_screenheight()

        # find the center point
        center_x = int(screen_width / 2 - WINDOW_WIDTH / 2)
        center_y = int(screen_height / 2 - WINDOW_HEIGHT / 2)

        # set the position of the window to the center of the screen
        ws.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{center_x}+{center_y}')

        # set background color
        ws.config(bg="#00CD33")

        # functions
        def get_entries():
            city_depart_check = city_depart.get()
            iata_depart_check = iata_depart.get()
            city_arr_check = city_arr.get()
            iata_arr_check = iata_arr.get()
            max_price_check = max_price.get()
            days_count_check = days_count.get()
            num_of_passengers_check = num_of_passengers.get()

            check_count = 0

            # check entries, if empty show warning
            f = FlightSearch()
            if city_depart_check == "":
                warn = "City of departure can't be empty!"
                messagebox.showwarning("Warning", warn)
            else:
                if iata_depart_check == "":
                    # get iata code if not provided, gives warning if no city iata found
                    iata_depart_check = f.get_location_code(city_depart_check)
                    print("iata_depart_check:", iata_depart_check)
                    if iata_depart_check != 0:
                        check_count += 1
                    else:
                        warn = "City of departure not found!"
                        messagebox.showwarning("Warning", warn)
                else: #TODO A SMALL FIX - IDIOT PROOF IT
                    check_count += 1

            if city_arr_check == "":
                warn = "City of arrival can't be empty!"
                messagebox.showwarning("Warning", warn)
            else:
                if iata_arr_check == "":
                    # get iata code if not provided, gives warning if no city iata found
                    iata_arr_check = f.get_location_code(city_arr_check)
                    print("iata_arr_check:", iata_arr_check)
                    if iata_arr_check != 0:
                        check_count += 1
                    else:
                        warn = "City of arrival not found!"
                        messagebox.showwarning("Warning", warn)
                else: #TODO A SMALL FIX - IDIOT PROOF IT
                    check_count += 1

            if max_price_check == "":
                warn = "Price can't be empty!"
                messagebox.showwarning("Warning", warn)
            else:
                check_count += 1
            if days_count_check == "":
                warn = "Number of days can't be empty"
                messagebox.showwarning("Warning", warn)
            else:
                check_count += 1
            if num_of_passengers_check == "":
                warn = "Number of passengers can't be empty"
                messagebox.showwarning("Warning", warn)
            else:
                check_count += 1

            # if all necessary data received (check count = 5) do:
            if check_count == 5:
                return True, iata_depart_check, iata_arr_check
            else:
                return False, iata_depart_check, iata_arr_check

        def save_filters():
            #TODO
            # if email in database check password
            # if password correct save as new entry
            # else password incorrect show warning
            # else email not in database save as a new entry

            # save filters to a database


            # get user input
            email_check = email.get()
            password_check = password.get()

            check_count = 0

            # checks if provided email field not empty if it is show warning
            if email_check == "":
                warn = "Email can't be empty!"
                messagebox.showwarning("Warning", warn)
            else:
                check_count += 1
                self.user_email = email_check

            # checks if password field empty, if not hashes password
            if password_check == "":
                warn = "Password can't be empty!"
                messagebox.showwarning("Warning", warn)
            else:
                check_count += 1
                self.user_password = hash_password(password_check)

            # when password and email provided are in the database if not = display warning message
            if check_count == 2:
                record_in_database = False
                returned_results = DatabaseManager().search_database('Email', email_check)  # searches database
                print("returned results nad  not in", returned_results)
                print("self. user email:", self.user_email)
                # if email not in database:
                if returned_results.empty:
                    #TODO add a new record to database with email, hashed password and all other needed data
                    print("email not in database")

                    city_depart_check = city_depart.get()
                    city_arr_check = city_arr.get()
                    max_price_check = max_price.get()
                    days_count_check = days_count.get()
                    num_of_passengers_check = num_of_passengers.get()

                    check_count, iata_depart_check, iata_arr_check = get_entries()

                    if check_count:
                        #save to a database

                        td = DateData(int(days_count_check))
                        next_date = td.next_date

                        dbM = DatabaseManager()
                        dbM.update_file(email=self.user_email, password=self.user_password,
                                                      city=city_arr_check, iata=iata_arr_check,
                                                      maxprice=max_price_check, dep_city=city_depart_check,
                                                      dep_iata=iata_depart_check, people=num_of_passengers_check,
                                                      days_range=days_count_check, next_date=next_date)
                        dbM.save_data_to_file()


                        info = "Successfully created new entry."
                        messagebox.showinfo("Info", info)

                    else:
                        warn = "Not all boxes filled correctly."
                        messagebox.showwarning("Warning", warn)

                #TODO
                # if email is in database:
                # if password matches email in the database:
                # add a new record to database with email, hashed password and all other needed data
                # if password doesn't match email in the database:
                # give warning incorrect credentials
                # if email not in database:
                # add a new record to database with email, hashed password and all other needed data

                else:
                    print("email in database")
                    flights = []
                    links = []
                    for index, row in returned_results.iterrows():
                        print("index, row", index, row)
                        if row['Password'] == self.user_password and row[
                            'Email'] == self.user_email:  # checks if password matches email in the database
                            record_in_database = True
                            print("password matches email")


                    if record_in_database:
                        #TODO add a new record to database with email, hashed password and all other needed data
                        print("email not in database")

                        city_depart_check = city_depart.get()
                        city_arr_check = city_arr.get()
                        max_price_check = max_price.get()
                        days_count_check = days_count.get()
                        num_of_passengers_check = num_of_passengers.get()

                        check_count, iata_depart_check, iata_arr_check = get_entries()

                        if check_count:
                            # save to a database

                            td = DateData(int(days_count_check))
                            next_date = td.next_date

                            dbM = DatabaseManager()

                            dbM.update_file(email=self.user_email, password=self.user_password,
                                                          city=city_arr_check, iata=iata_arr_check,
                                                          maxprice=max_price_check, dep_city=city_depart_check,
                                                          dep_iata=iata_depart_check, people=num_of_passengers_check,
                                                          days_range=days_count_check, next_date=next_date)
                            dbM.save_data_to_file()

                            info = "Successfully saved"
                            messagebox.showinfo("Info", info)

                        else:
                            warn = "Not all boxes filled correctly."
                            messagebox.showwarning("Warning", warn)

                    else:
                        warn = "Provided credentials incorrect."
                        messagebox.showwarning("Warning", warn)

        def clr():
            # clear entries boxes
            city_depart.delete(0, END)
            iata_depart.delete(0, END)
            city_arr.delete(0, END)
            iata_arr.delete(0, END)
            max_price.delete(0, END)
            days_count.delete(0, END)
            num_of_passengers.delete(0, END)

        def search():
            # read from entries
            city_depart_check = city_depart.get()
            city_arr_check = city_arr.get()
            max_price_check = max_price.get()
            days_count_check = days_count.get()
            num_of_passengers_check = num_of_passengers.get()

            check_count, iata_depart_check, iata_arr_check = get_entries()

            # if all necessary data received (check count = True) do:
            if check_count:
                # prepare received data and search for flight
                results = PrepareDataToSearch().filter_from_user_input(city=city_arr_check, fly_to=iata_arr_check,
                        fly_from=iata_depart_check, days_range=days_count_check, price_to=max_price_check,
                        adults=num_of_passengers_check)  # znalezione loty raw
                print("results: ", results)
                # formats, filters received flight data
                formatted_data, link = FlightData().format_data(results)
                formatted_data_list = [formatted_data]
                print("formatted data, link: ", formatted_data, link)
                # print(formatted_data)
                # passes the flight data to show in the window
                self.flight_show(formatted_data_list, link) # formatted_data needs to be an list to propely show flight in text box

            else:
                warn = "Not all boxes filled correctly."
                messagebox.showwarning("Warning", warn)

        # frames
        frame = Frame(ws, padx=20, pady=20)
        frame.pack(expand=True)

        main_frame = Frame(ws, padx=20, pady=20, bg="#00CD33")
        main_frame.pack(expand=True)

        title_frame = Frame(main_frame, padx=20, pady=20, bg="#00CD33")
        title_frame.grid(column=0, row=0)

        label_entry_frame = Frame(main_frame, padx=20, pady=20, bg="#00CD33")
        label_entry_frame.grid(column=0, row=1)

        save_filters_frame = Frame(main_frame, padx=0, pady=0, bg="#00CD33")
        save_filters_frame.grid(column=0, row=2)

        buttons_frame = Frame(main_frame, padx=20, pady=10, bg="#00CD33")
        buttons_frame.grid(column=0, row=3)

        # labels
        Label(title_frame, text="Wyszukiwanie lotów", bg="#00CD33", fg="#000",
              font=("Calibri", "24", "bold")).grid(row=0, columnspan=3, pady=10)

        Label(label_entry_frame, text='MIEJSCOWOSC WYLOTU*', bg="#00CD33", fg="#000",
              font=("Calibri", "12")).grid(row=1, column=0, pady=5, sticky='w')
        Label(label_entry_frame, text='IATA LOTNISKA WYLOTU', bg="#00CD33", fg="#000",
              font=("Calibri", "12")).grid(row=2, column=0, pady=5, sticky='w')
        Label(label_entry_frame, text='MIEJSCOWOSC PRZYLOTU*', bg="#00CD33", fg="#000",
              font=("Calibri", "12")).grid(row=3, column=0, pady=5, sticky='w')
        Label(label_entry_frame, text='IATA LOTNISKA WYLOTU', bg="#00CD33", fg="#000",
              font=("Calibri", "12")).grid(row=4, column=0, pady=5, sticky='w')
        Label(label_entry_frame, text='MAKSYMALNA CENA*', bg="#00CD33", fg="#000",
              font=("Calibri", "12")).grid(row=5, column=0, pady=5, sticky='w')
        Label(label_entry_frame, text='ZAKRES DNI*', bg="#00CD33", fg="#000",
              font=("Calibri", "12")).grid(row=6, column=0, pady=5, sticky='w')
        Label(label_entry_frame, text='LICZBA PASAŻERÓW*', bg="#00CD33", fg="#000",
              font=("Calibri", "12")).grid(row=7, column=0, pady=5, sticky='w')

        # label for saving filters
        Label(save_filters_frame, text='EMAIL', bg="#00CD33", fg="#000",
              font=("Calibri", "12")).grid(row=0, column=0, pady=0, padx=5, sticky='w')
        Label(save_filters_frame, text='HASŁO', bg="#00CD33", fg="#000",
              font=("Calibri", "12")).grid(row=0, column=1, pady=0, padx=5, sticky='w')

        # entry
        city_depart = Entry(label_entry_frame, width=30)
        iata_depart = Entry(label_entry_frame, width=30)
        city_arr = Entry(label_entry_frame, width=30)
        iata_arr = Entry(label_entry_frame, width=30)
        max_price = Entry(label_entry_frame, width=30)
        days_count = Entry(label_entry_frame, width=30)
        num_of_passengers = Entry(label_entry_frame, width=30)

        city_depart.grid(row=1, column=1)
        iata_depart.grid(row=2, column=1)
        city_arr.grid(row=3, column=1)
        iata_arr.grid(row=4, column=1)
        max_price.grid(row=5, column=1)
        days_count.grid(row=6, column=1)
        num_of_passengers.grid(row=7, column=1)

        # entry for saving filters
        email = Entry(save_filters_frame, width=20)
        email.grid(row=1, column=0, padx=5)
        password = Entry(save_filters_frame, width=20)
        password.grid(row=1, column=1, padx=5)

        # button
        clr = Button(buttons_frame, text="WYCZYŚĆ", padx=20, pady=10, relief=SOLID, font=("Calibri", "14", "bold"),
                     command=clr)
        reg = Button(buttons_frame, text="WYSZUKAJ", padx=20, pady=10, relief=SOLID, font=("Calibri", "14", "bold"),
                     command=search)
        ext = Button(buttons_frame, text="WYJDŹ", padx=20, pady=10, relief=SOLID, font=("Calibri", "14", "bold"),
                     command=lambda: ws.destroy())

        clr.grid(row=6, column=0, pady=20, padx=5)
        reg.grid(row=6, column=1, pady=20, padx=5)
        ext.grid(row=6, column=2, pady=20, padx=5)

        # save entry filters button
        save_filters_button = Button(save_filters_frame, text="ZAPISZ KRYTERIA", padx=10, relief=RAISED,
                                     font=("Calibri", "10", "bold"), command=save_filters)
        save_filters_button.grid(row=1, column=2, padx=5)

        ws.mainloop()


# g = GUI()