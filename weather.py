import csv
from datetime import datetime
import os

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    #First I have taken the date string and converted it to a datetime object using .strptime(): 
    date = datetime.strptime(iso_string,"%Y-%m-%dT%H:%M:%S%z")
    #Then format it to display in the way required using .strftime().
    return date.strftime("%A %d %B %Y")


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    #Convert the temp_in_farenheit to a float, convert into celsius, then round it to 1dp.
    return round((((float(temp_in_farenheit) - 32) * 5) / 9),1)

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    #import the mean function from statistics module
    from statistics import mean
    #the numbers in the data are stored as strings. Convert each item in the list to a float, then calculate the mean
    return mean([float(any_num) for any_num in weather_data])


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

    #create a list of the data from csv file
    with open(csv_file, 'r') as file: #open file in reading mode
        imported_file = list(csv.reader(file))
        #remove empty rows
        imported_file = [_ for _ in imported_file if _ != []]
        #convert string temps in second and third columns into integers:
        for i in range(1,len(imported_file)):
            for j in range(1,3):
                imported_file[i][j] = int(imported_file[i][j]) 
        #remove header row
        return imported_file[1:]

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    pass


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass