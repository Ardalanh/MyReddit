from django.test import TestCase
from django.core.urlresolvers import reverse
from django.urls import resolve
from .views import home

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        respone = self.client.get(url)
        self.assertEquals(respone.status_code, 200)

    def test_home_url_resolves_hoe_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)
# Create your tests here.
