import json

import requests_mock
from django.test import TestCase

from mailchimp3 import Mailchimp


class MailchimpTests(TestCase):
    datacenter = "us6"
    key = "c08ab581ee15d1d9e53fb4e6715e6c2b-" + datacenter

    def setUp(self):
        self.mc = Mailchimp(self.key)

    def test_post_api(self):
        fake_endpoint = 'endpoint/to/match'
        fake_request = {'hirondelle': 'Test'}
        fake_response = {'status': 'Test Succeeded'}

        # Mock the Mailchimp endpoint
        with requests_mock.mock() as m:
            m.post(
                'https://' + self.datacenter + '.api.mailchimp.com/3.0/' + fake_endpoint,
                text=json.dumps(fake_response)
            )

            response = self.mc.post_api(fake_endpoint, fake_request)
            self.assertTrue(m.called)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), fake_response)
