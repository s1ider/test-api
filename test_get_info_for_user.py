import requests
from base_test import BaseAPITest


class TestGetInfoForUser(BaseAPITest):

    def setUp(self):
        super(TestGetInfoForUser, self).setUp()
        self.url = self.base_url + '/user/current'

    def test_get_info_for_current_user(self):
        r = requests.get(self.url, cookies=self.cookies)
        self.assertEqual(r.status_code, 200)