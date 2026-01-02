import requests
import json

AMADEUS_ENDPOINT = "https://test.api.amadeus.com"

class FlightSearch:
    def __init__(self, amadeus_sensitive_data):
        amadeus_token_endpoint = f"{AMADEUS_ENDPOINT}/v1/security/oauth2/token"

        self.sensitive_data = amadeus_sensitive_data

        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        autohrization_data = {
            "grant_type": "client_credentials",
            "client_id": amadeus_sensitive_data["api_key"],
            "client_secret": amadeus_sensitive_data["api_secret"]
        }

        response = requests.post(url=amadeus_token_endpoint, headers=header, data=autohrization_data)
        print(response.text)
        token = response.json()["access_token"]

        self.headers = {
            "Authorization": f"Bearer {token}"
        }
        
    
    #---------------------------------------------------------------------
    # CITY IATA CODE SEARCH
    #---------------------------------------------------------------------
    def search_iata_codes(self, city_name):
        city_search_endpoint =f
        city_search_params = {
            "keyword": city_name,
        }

        response = requests.get(url=city_search_endpoint, headers=self.headers, params=city_search_params)
        iata_code = response.json()["data"][0]["iataCode"]

        return iata_code


    #---------------------------------------------------------------------
    # FLIGHT SEARCH
    #---------------------------------------------------------------------
    def search_flight_prices(self, origin, destination):
        flight_search_endpoint = f"{AMADEUS_ENDPOINT}/v2/shopping/flight-destinations"
        print(origin)
        flight_params = {
            "origin": origin,
        }

        response = requests.get(url=flight_search_endpoint, headers=self.headers, params=flight_params)
        print(response.text)
        

    def get_destination_code(self, city_name):
        print(f"Using this token to get destination {self._token}")
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(
            url=f"{AMADEUS_ENDPOINT}/v1/reference-data/locations/cities",
            headers=headers,
            params=query
        )
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code


    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):

        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(
            url=f"{AMADEUS_ENDPOINT}/v2/shopping/flight-destinations",
            headers=self.headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()
