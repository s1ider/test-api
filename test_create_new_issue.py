import requests
from base_test import BaseAPITest
from yaml import load

class TestCreateNewIssue(BaseAPITest):

    def setUp(self):
        super(TestCreateNewIssue, self).setUp()
        self.url = self.base_url + '/issue/'

    def test_new_issue(self):
        params = {
            'project': 'API',
            'summary': 'Testszf summary from robots',
            'description': 'Hail the robots'
        }
        r = requests.put(self.url, data=params, cookies=self.cookies)
        issue_id = r.headers['location'].split('/')[-1]

        self.assertEquals(r.status_code, 201)

        r = requests.get(self.url + issue_id, cookies=self.cookies)
        self.assertEquals(r.status_code, 200)

    def test_new_issue_with_incorrect_project(self):
        params = {
            'project': 'IAMINVALID',
            'summary': 'Test summary from robots',
            'description': 'Hail the robots'
        }
        r = requests.put(self.url, data=params, cookies=self.cookies)
        self.assertEquals(r.status_code, 403)
