from django.test import TestCase

# Create your tests here.
class SimpleTests(TestCase):
    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # def test_post_page(self):
    #     response = self.client.get("/post/")
    #     self.assertEqual(response.status_code, 200)
    
    def test_newposts_page(self):
        response = self.client.get("/new/")
        self.assertEqual(response.status_code, 200)
        
    def test_askhn_page(self):
        response = self.client.get("/ask-hn/")
        self.assertEqual(response.status_code, 200)

    def test_showhn_page(self):
        response = self.client.get("/show-hn/")
        self.assertEqual(response.status_code, 200)

    def test_hnjobs_page(self):
        response = self.client.get("/hn/jobs/")
        self.assertEqual(response.status_code, 200)

    def test_hnpolls_page(self):
        response = self.client.get("/hn/polls/")
        self.assertEqual(response.status_code, 200)