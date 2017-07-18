"""
Mailchimp integration, APIv3

By @msuixo <suixo@securem.eu>
"""
import logging

import requests

from . import app_settings


class Mailchimp(object):
    def __init__(self):
        # Build the API URL from the API Key
        self.api_key = app_settings.MAILCHIMP_API_KEY
        datacenter = self.api_key[self.api_key.find('-') + 1:]
        self.api_url = app_settings.MAILCHIMP_API_URL.format(
            datacenter=datacenter
        )

    def add_member_to_list(self, list_id, email_address, status="subscribed"):
        """ Add email_address to the list list_id, setting the given status """
        json = {
            'email_address': email_address,
            'status': status,
        }
        response = self._post_api('lists/' + list_id + '/members', json)
        return response.status_code == 200

    def _post_api(self, endpoint, json):
        logging.debug("Send POST payload to {}".format(endpoint))
        response = requests.post(
            self.api_url + endpoint,
            json=json,
            auth=('mailchimp3lib', self.api_key),
        )
        logging.debug(
            "Got response {} for {}".format(response.status_code, endpoint)
        )
        return response
