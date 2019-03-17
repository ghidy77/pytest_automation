import requests
from utilities.globals import Globals
import utilities.custom_logger as cl
import logging


class ApiClient():

    ACCEPT_HEADER = {
        "items" : {
            "Accept": "application/items+json; version=2.0.0"
        },
        "users" : {
            'Accept': 'application/users+json; version=1.0.0'
        },
    }

    log = cl.customLogger(logging.DEBUG)

    def __init__(self):
        self.baseURL = 'https://example.com/'

    def get(self, path, body, headers = {}, useAuthorizationBearer = True):
        if useAuthorizationBearer:
            headers["Authorization"] = "Bearer " + Globals.accessToken

        response = requests.get(self.baseURL + path, json=body, headers=headers)

        self.log.info("GET: " + path + ", response: " + str(response.status_code))

        body = response.json()
        # print(body)
        return body

    def put(self, path, body, headers = {}, useAuthorizationBearer = True):
        if useAuthorizationBearer:
            headers["Authorization"] = "Bearer " + Globals.accessToken

        response = requests.put(self.baseURL + path, json=body, headers=headers)

        self.log.info("PUT: " + path + " Response: " + str(response.status_code))

        # body = response.json()
        return response.status_code

    def post(self, path, body, headers = {}, useAuthorizationBearer = True):
        if useAuthorizationBearer:
            headers["Authorization"] = "Bearer " + Globals.accessToken

        response = requests.post(self.baseURL + path, json=body, headers=headers)

        self.log.info("POST: " + path + ", response: " + str(response.status_code))

        body = response.json()
        return body