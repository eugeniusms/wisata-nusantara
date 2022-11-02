from django.test import TestCase, Client
class TestDaftarEventViews(TestCase):
  def test_daftar_event(self):         
      response = Client().get('/event/')
      self.assertEquals(response.status_code,200)