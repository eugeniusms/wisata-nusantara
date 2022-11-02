from django.test import TestCase, Client
class TestCeritaPerjalananViews(TestCase):
  def test_cerita_perjalanan(self):         
      response = Client().get('/story/')
      self.assertEquals(response.status_code,200)