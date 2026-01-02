import requests

class DataManager:

    def __init__(self, sheety_sensitive_data):
        self.sensitive_data = sheety_sensitive_data
        self.headers = {
            "Authorization": sheety_sensitive_data["Authorization"]
        }
        self.get_endpoint = sheety_sensitive_data["sheety_get_endpoint"]
        self.put_endpoint = sheety_sensitive_data["sheety_put_endpoint"]
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=self.get_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=self.put_endpoint,
                json=new_data
            )
            print(response.text)
