from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class SendMessageTestCase(TestCase):

    def setUp(self):
        self.url = reverse('courses:send_message')
        self.client = Client()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)