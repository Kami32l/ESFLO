from datetime import datetime


class DateData:
    """
    This class is responsible for structuring the dates, finding today and next date.
    :param days: number representing range of days (from 1 to 365).
    :return:
    """

    def __init__(self, days):
        """
        Initialazing method, takes care of finding current date.
        :param days: number of days into the future to look for a flight
        """
        # takes care of finding dates.
        self.today = datetime.now()

        self.today_year = self.today.year
        self.today_month = self.today.month
        self.today_day = self.today.day

        self.today_date = datetime.now().date().strftime("%d/%m/%Y")

        self.days_ahead = days - 1      # -1 - counts from today without it counts days from tomorrow
        self.days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.days_from_start_of_the_year = 0

        self.next_year_days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        self.next_year = 0
        self.next_month = 0
        self.next_day = 0

        self.next_date = ""

        self.leap = self.is_year_leap(self.today_year, 1)
        self.leap_next_year = self.is_year_leap(self.today_year, 0)
        self.find_date_from_start_of_the_year()
        # print("days from start of the year ", self.next_date)

    def is_year_leap(self, year, activator):
        """
        Checks if year is  a leap year
        :param year: a year (2000 or 934)
        :param activator: if "0" - today date, if "1" - next date
        :return: returns True if year is a leap year or False otherwise
        """

        if year % 4 == 0 and not year % 100 == 0 or year % 100 == 0 and year % 400 == 0:
            if activator == 1:
                self.days_in_months[1] = 29
            elif activator == 0:
                self.next_year_days_in_months[1] = 29
            return True
        else:
            return False

    def find_date_from_start_of_the_year(self):
        """
        Finds out the date in 'days' number of days from today.
        :return:
        """

        # calculates days from start of the year
        try:
            months_scope = self.days_in_months[0:self.today_month - 1]
        except IndexError:
            months_scope = self.days_in_months

        for days in months_scope:
            self.days_from_start_of_the_year += days
        self.days_from_start_of_the_year += self.today_day
        days = self.days_from_start_of_the_year + self.days_ahead

        # print("Number of days from start of the year has has calculated:", self.days_from_start_of_the_year, )
        # print("Days to given date from start of the year:", days)

        # checks if date will be in the next year

        if self.leap:
            # calculates dates for leap year

            # if days from start of the year exceed 366 (for a leap year) - it means it is next year
            if days > 366:
                # print("day in the next year - leap year")

                days -= 366

                # checks which month of the year
                month_days_sum = 0
                i = 0
                equal = False
                for days_in_month in self.days_in_months:
                    if days > month_days_sum:
                        month_days_sum += days_in_month
                        i += 1
                    elif days == month_days_sum:
                        equal = True
                        month_days_sum += days_in_month
                        i += 1
                    else:
                        pass
                        # print("days sum:", month_days_sum, "days: ", days, "month: ", i)

                if equal:
                    self.next_month = i - 1
                else:
                    self.next_month = i

                self.next_day = abs(month_days_sum - days - 1)  # abs(days - (month_days_sum -
                # - self.days_in_months[self.next_month - 1]))
                self.next_year = self.today_year + 1
                self.next_date = f"{self.next_day}/{self.next_month}/{self.next_year}"

                # self.print_function_for_debugging(days, days_in_month)

            else:
                # if days from start of the year lower or equal to 366 (for a leap year) - it means it is current year

                # print("day in this year - leap year")

                # checks which month of the year
                month_days_sum = 0
                i = 0
                equal = False
                for days_in_month in self.days_in_months:
                    if days > month_days_sum:
                        month_days_sum += days_in_month
                        i += 1
                    elif days == month_days_sum:
                        equal = True
                        month_days_sum += days_in_month
                        i += 1
                    else:
                        pass
                        # print("days sum:", month_days_sum, "days: ", days, "month: ", i)

                if equal:
                    self.next_month = i - 1
                else:
                    self.next_month = i

                self.next_day = abs(month_days_sum - days - 1)
                self.next_year = self.today_year
                self.next_date = f"{self.next_day}/{self.next_month}/{self.next_year}"

                # self.print_function_for_debugging(days, days_in_month)

        else:
            # calculates dates for standard year

            # if days from start of the year exceed 365 - it means it is next year
            if days > 365:
                # print("day in the next year - standard year")
                days -= 365

                # checks which month of the year
                month_days_sum = 0
                i = 0
                equal = False
                for days_in_month in self.days_in_months:
                    if days > month_days_sum:
                        month_days_sum += days_in_month
                        i += 1
                    elif days == month_days_sum:
                        equal = True
                        month_days_sum += days_in_month
                        i += 1
                    else:
                        pass
                        # print("days sum:", month_days_sum, "days: ", days, "month: ", i)

                if equal:
                    self.next_month = i - 1
                else:
                    self.next_month = i

                self.next_day = self.days_in_months[self.next_month - 1] - abs(month_days_sum - days - 1)
                self.next_year = self.today_year + 1
                self.next_date = f"{self.next_day}/{self.next_month}/{self.next_year}"

                # self.print_function_for_debugging(days, days_in_month)

            # if days from start of the year lower or equal to 365 - it means it is current year
            else:
                # print("day in this year - standard year")

                # checks which month of the year
                month_days_sum = 0
                i = 0
                equal = False
                for days_in_month in self.days_in_months:
                    if days > month_days_sum:
                        month_days_sum += days_in_month
                        i += 1
                    elif days == month_days_sum:
                        equal = True
                        month_days_sum += days_in_month
                        i += 1
                    else:
                        pass
                        # print("days sum:", month_days_sum, "days: ", days, "month: ", i)

                if equal:
                    self.next_month = i - 1
                else:
                    self.next_month = i

                self.next_day = self.days_in_months[self.next_month - 1] - abs(month_days_sum - days - 1)
                self.next_year = self.today_year
                self.next_date = f"{self.next_day}/{self.next_month}/{self.next_year}"

                # self.print_function_for_debugging(days, days_in_month)

    def print_function_for_debugging(self, days, month_days_sum):
        """
        Function used only for debugging during development (printing some values in console), after finding both dates.
        :param days:
        :param month_days_sum:
        :return:
        """

        print("Self.next_month:", self.next_month)
        print("Self.days_in_months[self.next_month-1]:", self.days_in_months[self.next_month - 1])
        print("Days:", days)
        print("Month_days_sum:", month_days_sum)
        print("Self.next_day:", self.next_day)
        print(self.next_date)
