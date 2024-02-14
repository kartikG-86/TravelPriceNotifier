from pprint import pprint
import requests
import datetime as dt
from flight_data import FlightData
FLIGHT_SEARCH_API_KEY = "lSoPIT3Jlf2LXUcVuKc08KU2xnD0P7q0"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
tomorrow_date = dt.datetime.now() + dt.timedelta(days=1)
tomorrow_date = tomorrow_date.strftime("%d/%m/%Y")
after_6_month_date = dt.datetime.now() + dt.timedelta(days= 6*30)
after_6_month_date = after_6_month_date.strftime("%d/%m/%Y")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass
    def get_destination_code(self,city):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        header = {
            "apikey":FLIGHT_SEARCH_API_KEY
        }
        parameters = {
            "term":city,
            "location_types":"city"
        }
        response = requests.get(url=location_endpoint,headers=header,params=parameters)
        print(response.json())
        code = response.json()["locations"][0]["code"]
        return code

    def search_flight(self,origin_city_iata,destination_iata):

            flight_search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"


            header = {
                "apikey":FLIGHT_SEARCH_API_KEY

            }
            parameters = {
                "fly_from": origin_city_iata,
                "fly_to": destination_iata,
                "date_from": tomorrow_date,
                "date_to": after_6_month_date,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "max_stopovers": 0,
                "curr": "GBP"
            }

            response = requests.get(url=flight_search_endpoint,headers=header,params=parameters)

            try:
                data = response.json()["data"][0]
            except IndexError:
                # print(f"No flights found for {destination_iata}")
                parameters["max_stopovers"] = 2
                new_response = requests.get(url=flight_search_endpoint,headers=header,params=parameters)
                pprint(new_response.json())
                data = new_response.json()["data"][0]
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0]
                )
                flight_data.stop_overs = parameters["max_stopovers"] - 1
                flight_data.via_city = data["route"][0]["cityTo"]
                return flight_data
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0]
                )
                print(f"{flight_data.destination_city}: £{flight_data.price}")
                return flight_data




