"""
Mailchimp integration, APIv3

By @msuixo <suixo@securem.eu>
"""
import logging

import requests


class Mailchimp(object):
    API_URL = "https://{datacenter}.api.mailchimp.com/3.0/"

    def __init__(self, api_key):
        if len(api_key) < 35 or api_key.find('-') == -1:
            raise ValueError(
                "Mailchimp Api Key should be at least 35 characters"
                " and contain a dash."
            )
        self.api_key = api_key
        datacenter = api_key[api_key.find('-') + 1:]
        self.api_url = self.API_URL.format(datacenter=datacenter)

    def add_member_to_list(self, list_id, email_address, status="subscribed"):
        """ Add email_address to the list list_id, setting the given status """
        json = {
            'email_address': email_address,
            'status': status,
        }
        response = self._post_api('lists/' + list_id + '/members', json)
        logging.info(response.json()['detail'])
        return response.status_code == 200

    def _post_api(self, endpoint, json):
        logging.debug("Send POST payload to {}".format(endpoint))
        response = requests.post(
            self.api_url + endpoint,
            json=json,
            auth=('mailchimp3lib', self.api_key),
        )
        logging.debug("Got response {} for {}".format(
            response.status_code, endpoint))
        return response
