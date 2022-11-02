from django.test import TestCase, Client
class TestFaqViews(TestCase):
  def test_faq(self):         
      response = Client().get('/faq/')
      self.assertEquals(response.status_code,200)