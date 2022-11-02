from django.test import TestCase, Client
class TestPanduanPerjalananViews(TestCase):
  def test_panduan_perjalanan(self):         
      response = Client().get('/journey/')
      self.assertEquals(response.status_code,200)