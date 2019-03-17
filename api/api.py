import requests
import time
from datetime import datetime
from base.basepage import BasePage
from utilities.globals import Globals
from utilities.api_client import ApiClient
import utilities.custom_logger as cl
import logging
import fileinput
import urllib3
from urllib.parse import urlencode
import json
from json import JSONEncoder


class ApiMethods(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.api = ApiClient()

    def login(self, username, password):
        oauth_client_id = 'CLIENT_ID'
        oauth_client_secret = 'SECRET_KEY'

        query_param = {
                'client_id': oauth_client_id,
                'client_secret': oauth_client_secret,
                'grant_type': 'password',
                'scope': 'public root',
                'username': username,
                'password': password

        }
		
        response = self.api.post("v1/oauth2/token",query_param,useAuthorizationBearer=False)
        # print(response)
        Globals.accessToken = response['access_token']
		
		action = "action_example"
		self.api.put("user-actions/" + action, body={}, self.api.ACCEPT_HEADER["user-actions"])


    def getItem(self, item_id):

		self.log.info('GET ITEM: ' + json.dumps(response))
		
        response = self.api.get("media/" + item_id + "?extra_params=true", body={}, headers=self.api.ACCEPT_HEADER["items"])
		assert response["item_name"] == 'correct name', "verify the name of the item"
		return item_id

