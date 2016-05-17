import requests
from base_test import BaseAPITest


class TestUpdateIssue(BaseAPITest):

    def setUp(self):
        super(TestUpdateIssue, self).setUp()
        self.url = self.base_url + '/issue/'

    def test_update_issue(self):
        issue_id = self.create_issue()
        params = {
            'summary': 'Test updated summary',
            'description': 'Test updated description'
        }

        r = requests.post(self.url + issue_id, data=params, cookies=self.cookies)
        self.assertEqual(r.status_code, 200)

    def test_update_issue_with_no_data(self):
        issue_id = self.create_issue()
        params = {}
        r = requests.post(self.url + issue_id, data=params, cookies=self.cookies)
        self.assertEqual(r.status_code, 400)