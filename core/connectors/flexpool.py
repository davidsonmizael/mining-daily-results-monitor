import requests
import json

from core.connectors.http_handler import get_request, get_json_headers

class Flexpool():

    def __init__(self, logger, base_url, wallet, coin):
        self.logger = logger
        self.base_url = base_url
        self.coin = coin
        self.wallet = wallet

    def check_balance(self):
        url = self.base_url + 'miner/balance'

        params = { 
            "coin": self.coin,
            "address": self.wallet
        }

        headers = get_json_headers(self.logger)

        return get_request(self.logger, url, parameters=params, headers=headers, return_json=True)


    def check_status(self):
        url = self.base_url + 'miner/balance'

        params = { 
            "coin": self.coin,
            "address": self.wallet
        }

        headers = get_json_headers(self.logger)

        return get_request(self.logger, url, parameters=params, headers=headers, return_json=True)
