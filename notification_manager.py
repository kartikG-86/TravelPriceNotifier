import os
import requests
from twilio.rest import Client
from flight_data import FlightData
import smtplib

BEARER = "kjshdkfuydslif9dsflsdhfit8yfkdsjf"

user_sheet_endpoint = "https://api.sheety.co/0ce0dbde97b66e43a74aa0fab3a9085e/user'sClubSheet/sheet1"
headers = {
    "Authorization": f"Bearer {BEARER}",
    "Content-Type": "application/json",
}
email = "kartikgoyal0852@gmail.com"
password = "dgzfvqbpznsbcrry"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = "AC08bb64f248a60b3ddf05a788110d3742"
        self.auth_token = "039314600ac97818ebb29344e66193e7"
        self.client = Client(self.account_sid, self.auth_token)

    def sent_message(self,flight:FlightData):
        if flight.stop_overs == 0:
            message = self.client.messages \
                    .create(
                         body=f"Low Price Alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}",
                         from_='+18564914786',
                         to='+919958919447'
                     )
            print(message.sid)
        else:
            message = self.client.messages \
                    .create(
                         body=f"Low Price Alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date} \n\n Flight has {flight.stop_overs} stop over, via {flight.via_city} City",
                         from_='+18564914786',
                         to='+919958919447'
                     )
            print(message.sid)

    def send_mail(self,flight:FlightData):
        users = requests.get(url=user_sheet_endpoint,headers=headers)
        for customer in users.json()["sheet1"]:

            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=email,password=password)
                if flight.stop_overs == 0:
                    connection.sendmail(from_addr=email,to_addrs=customer["email"],msg=f"Subject: Low Price Alert! \n\n Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}".encode('utf-8'))
                else:
                    connection.sendmail(from_addr=email,to_addrs=customer["email"],msg=f"Subject: Low Price Alert! \n\n Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date} \n\n Flight has {flight.stop_overs} stop over, via {flight.via_city} City".encode('utf-8'))


