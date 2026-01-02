import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    #---------------------------------------------------------------------
    # ADD IATA CODE TO SHEET
    #---------------------------------------------------------------------
    def __init__(self, sheety_sensitive_data):
        self.sensitive_data = sheety_sensitive_data
        self.headers = {
            "Authorization": sheety_sensitive_data["Authorization"]
        }
        self.get_endpoint = sheety_sensitive_data["sheety_get_endpoint"]
        self.put_endpoint = sheety_sensitive_data["sheety_put_endpoint"]

    def get_sheet_rows(self): 
        response = requests.get(url=self.get_endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()["prices"]
    
    def update_sheet_row(self, row_id, sheety_updated_row):
        response = requests.put(url=f"{self.put_endpoint}{row_id}", json=sheety_updated_row, headers=self.headers)
        print(response.text)

    def get_iata_codes(self):
        response = requests.get(url=self.get_endpoint, headers=self.headers)
        response.raise_for_status()
        iata_codes = []
        for row in response.json()["prices"]:
            iata_codes.append(row["iataCode"])
            
        return iata_codes
