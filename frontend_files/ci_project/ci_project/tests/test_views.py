from django.test import TestCase,override_settings,Client



class TestViewResponses(TestCase):
    def setUp(self):
        self.client =Client()

    def test_home_url(self):
        """Test home response status"""
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_contact_us_url(self):
        response = self.client.get('/contactUs/')
        self.assertEqual(response.status_code,200)
        
    def test_about_url(self):
        """Test about response status"""
        response = self.client.get('/about/')
        self.assertEqual(response.status_code,200)