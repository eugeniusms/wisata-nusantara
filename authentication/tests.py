from django.test import TestCase, Client
class TestAuthenticationViews(TestCase):
  def test_login(self):         
      response = Client().get('/auth/login/')
      self.assertEquals(response.status_code,200)

  def test_register(self):         
      response = Client().get('/auth/register/')
      self.assertEquals(response.status_code,200)
    
