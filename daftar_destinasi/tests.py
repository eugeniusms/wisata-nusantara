from django.test import TestCase, Client
class TestDaftarDestinasiViews(TestCase):
  def test_daftar_destinasi(self):         
      response = Client().get('/destination/')
      self.assertEquals(response.status_code,200)

  def test_wishlist(self):         
      response = Client().get('/wishlist/')
      self.assertEquals(response.status_code,200)
    
