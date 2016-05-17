import requests
from base_test import BaseAPITest


class TestGetUserByLogin(BaseAPITest):

    def setUp(self):
        super(TestGetUserByLogin, self).setUp()
        self.url = self.base_url + '/user/'

    def test_get_user_by_login_name(self):
        r = requests.get(self.url + 'root', cookies=self.cookies)
        self.assertEqual(r.status_code, 200)

    def test_get_user_by_invalid_login_name(self):
        r = requests.get(self.url + 'test', cookies=self.cookies)
        self.assertEqual(r.status_code, 403)