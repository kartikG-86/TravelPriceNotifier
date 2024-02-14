import requests
flight_google_sheet_endpoint = "https://api.sheety.co/0ce0dbde97b66e43a74aa0fab3a9085e/personalFlightSearch/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):

        self.update_sheet_endpoint = "https://api.sheety.co/0ce0dbde97b66e43a74aa0fab3a9085e/personalFlightSearch/prices"
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=flight_google_sheet_endpoint)
        self.destination_data = response.json()["prices"]
        return self.destination_data


    def update_destination_codes(self):
        for item in self.destination_data:
            update_data = {
                "price" : {
                    "iataCode" : item["iataCode"]
                }
            }
            response = requests.put(url=f"{self.update_sheet_endpoint}/{item["id"]}",json=update_data)
            print(response.raise_for_status())

    def new_city(self,city,iata,lowestPrice):
        # add new data in sheet

        data = {
            "price":{
                "city":city,
                "iataCode":iata,
                "lowestPrice":lowestPrice

            }
        }
        new_data_response = requests.post(url=flight_google_sheet_endpoint,json=data)
        print(new_data_response.text)
