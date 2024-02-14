import datetime as dt
import requests
SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2"
API_KEY = "lSoPIT3Jlf2LXUcVuKc08KU2xnD0P7q0"

from pprint import pprint


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stop_overs = 0
        self.via_city = ""



