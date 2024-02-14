#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from flight_search import FlightSearch
from data_manager import DataManager
dataManager = DataManager()
# add new Data
dataManager.new_city(city="Bali",iata="DPS",lowestPrice=1000)

sheet_data = dataManager.get_destination_data()
from pprint import pprint # it is use to format the data
flightSearch = FlightSearch()
ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == '':
    flightSearch = FlightSearch()
    for item in sheet_data:
        if item["iataCode"] == '':
            item["iataCode"] = flightSearch.get_destination_code(item["city"])

    dataManager.destination_data = sheet_data
    dataManager.update_destination_codes()




for destination in sheet_data:
    flight = flightSearch.search_flight(ORIGIN_CITY_IATA,destination["iataCode"])

    if flight is None: # no data available
        continue
    elif flight.price < destination["lowestPrice"]:
        from notification_manager import NotificationManager
        notification = NotificationManager()
        notification.sent_message(flight)
        notification.send_mail(flight)


