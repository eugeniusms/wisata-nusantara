from django.test import TestCase, Client
class TestDashboardViews(TestCase):
  def test_dashboard(self):         
      response = Client().get('/')
      self.assertEquals(response.status_code,200)