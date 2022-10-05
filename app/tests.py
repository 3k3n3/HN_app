from django.test import TestCase
from django.urls import reverse
from .models import Base

# Create your tests here.

class HomePageViewTest(TestCase):
    def setUp(self):
        self.post = Base.objects.create(
            text='TESTING>>>',
            title = 'My Test',
            post_type='Ask HN',        
        )

    def test_str_representation(self):
        post = Base(title='A sample title', post_type='Ask HN')
        self.assertEqual(str(post), f'{post.title} ({post.post_type})')        

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'My Test')
        self.assertEqual(f'{self.post.text}', 'TESTING>>>')
        self.assertEqual(f'{self.post.post_type}', 'Ask HN')

    def test_post_list(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Test')
        self.assertTemplateUsed(response, 'app/home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        # no_response = self.client.get('/post/2/')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'My Test')
        self.assertTemplateUsed(response, 'app/post.html')

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/None/')
        # No posts yet else /post/1/

'''


    def setUp(self):
        Base.objects.create(text='TESTING>>>')

    def test_view_url_exists(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/home.html')


class ModelTest(TestCase):
    def setUp(self):
        Base.objects.create(text='TESTING>>>')

    def test_text_content(self):
        post = Base.objects.get(post_id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'TESTING>>>')


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
        '''