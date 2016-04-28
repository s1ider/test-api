import requests
from yaml import load
from base_test import BaseAPITest


class TestDeleteIssue(BaseAPITest):

    def setUp(self):
        super(TestDeleteIssue, self).setUp()
        self.url = self.base_url + '/issue/'

    def test_delete_issue(self):
        # create new test issue
        issue_id = self.create_issue()

        r = requests.delete(self.url + issue_id, cookies=self.cookies)
        self.assertEquals(r.status_code, 200)

        r = requests.get(self.url + issue_id, cookies=self.cookies)
        self.assertEquals(r.status_code, 404)

    def test_delete_unexisted_issue(self):
        issue_id = 'labuda'
        r = requests.delete(self.url + issue_id, cookies=self.cookies)
        self.assertEquals(r.status_code, 403)

