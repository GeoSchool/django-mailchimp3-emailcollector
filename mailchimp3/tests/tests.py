import json

import requests_mock
from django.test import TestCase

from .. import mailchimp
from .tests_utils import ExtraTestToolsMixin


class MailchimpTests(ExtraTestToolsMixin, TestCase):
    datacenter = "us6"
    key = "c08ab581ee15d1d9e53fb4e6711e6c2b-" + datacenter

    def setUp(self):
        with self.app_settings(mailchimp, MAILCHIMP_API_KEY=self.key):
            self.mc = mailchimp.Mailchimp()
        self.fake_endpoint = 'endpoint/to/match'
        self.fake_request = {'hirondelle': 'Test'}
        self.fake_response = {'status': 'Test Succeeded'}

    def test_add(self):
        """ Calling mc.add_member_to_list should trigger the API call """
        # Mock the Mailchimp endpoint
        with requests_mock.mock() as m:
            m.post(
                'https://' + self.datacenter +
                '.api.mailchimp.com/3.0/lists/listID/members',
                text=json.dumps(self.fake_response)
            )

            added = self.mc.add_member_to_list('listID', 'alfred@niel.edu')
            self.assertTrue(added)
            self.assertTrue(m.called)

    def test_post_api(self):
        # Mock the Mailchimp endpoint
        with requests_mock.mock() as m:
            m.post(
                'https://' + self.datacenter + '.api.mailchimp.com/3.0/' +
                self.fake_endpoint,
                text=json.dumps(self.fake_response)
            )

            response = self.mc._post_api(self.fake_endpoint, self.fake_request)
            self.assertTrue(m.called)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.fake_response)
