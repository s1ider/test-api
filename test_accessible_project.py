import requests
from base_test import BaseAPITest

class TestGetAccessibleProject(BaseAPITest):

    def setUp(self):
        super(TestGetAccessibleProject, self).setUp()
        self.url = self.base_url + '/project/'

    def test_get_accessible_project(self):
        r = requests.get(self.url + 'all', cookies=self.cookies)
        self.assertEqual(r.status_code, 200)
        print(r.text)
