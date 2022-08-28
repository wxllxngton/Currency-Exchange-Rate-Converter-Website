# Import necessary libraries
from __future__ import print_function
import time
import cloudmersive_currency_api_client
from cloudmersive_currency_api_client.rest import ApiException
from pprint import pprint

API_KEY = '1c75e0a3-7921-4133-b3f5-ff873da3b885'

class Converter:
    def __init__(self,source,destination):
        self.source = source
        self.destination = destination


    def convert(self):
        # Configure API key authorization: Apikey
        configuration = cloudmersive_currency_api_client.Configuration()
        configuration.api_key['Apikey'] = API_KEY
        # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
        # configuration.api_key_prefix['Apikey'] = 'Bearer'

        # create an instance of the API class
        api_instance = cloudmersive_currency_api_client.CurrencyExchangeApi(cloudmersive_currency_api_client.ApiClient(configuration))
        source = self.source # str | Source currency three-digit code (ISO 4217), e.g. USD, EUR, etc.
        destination = self.destination # str | Destination currency three-digit code (ISO 4217), e.g. USD, EUR, etc.

        try:
            # Gets the exchange rate from the source currency into the destination currency
            api_response = api_instance.currency_exchange_get_exchange_rate(source, destination)
            return str(api_response).split(' ')[1].split('}')[0]
        except ApiException as error:
            message = f"Exception when calling CurrencyExchangeApi->currency_exchange_get_exchange_rate: {error}"
            return message


