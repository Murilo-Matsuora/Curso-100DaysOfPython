import requests
import json
from flight_search import FlightSearch
from data_manager import DataManager

ORIGIN = "LON"

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


#---------------------------------------------------------------------
# CITY IATA CODE SEARCH AND ADDITION TO SHEET
#---------------------------------------------------------------------
def add_iata_codes_to_sheet():
    sheet_rows = sheets_data_manager.get_sheet_rows()
    for row in sheet_rows:
        row_id = row["id"]
        iata_code = flight_searcher.search_iata_codes(city_name=row["city"])
        
        sheety_updated_row = {
            "price": {
                "iataCode": f"{iata_code}",
            }
        }
        sheets_data_manager.update_sheet_row(row_id, sheety_updated_row=sheety_updated_row)


#---------------------------------------------------------------------
# READ SENSITIVE DATA
#---------------------------------------------------------------------
sensitive_data = {}
with open(file="sensitive_data.json", mode="r") as f:
    sensitive_data = json.load(f)


#---------------------------------------------------------------------
# CONNECT TO AMADEUS FLIGHTS API
#---------------------------------------------------------------------
flight_searcher = FlightSearch(sensitive_data["amadeus"])


#---------------------------------------------------------------------
# CONNECT TO SHEETY API
#---------------------------------------------------------------------
sheets_data_manager = DataManager(sensitive_data["sheety_data"])

# UPDATE IATA CODES IN THE SHEET
# add_iata_codes_to_sheet()

# SEARCH FOR CHEAP FLIGHTS
iata_codes = sheets_data_manager.get_iata_codes()
for iata_code in iata_codes:
    flight_searcher.search_flight_prices(origin=ORIGIN, destination=iata_code)





