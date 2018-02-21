from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
from annonces.models import Annonce
from user.models import Profile
from django.test import Client
import unittest, time


class UserTest(LiveServerTestCase):
    def setUp(self):

        self.browser = webdriver.Chrome("/Users/alexseymour/Documents/chromedriver")
        #self.fail(self.live_server_url)
        self.browser.implicitly_wait(3)
        self.new_user = User.objects.create_user(username="test_user", email="test@gmail.com", password="azerty")
        self.profile = Profile.objects.create(user=self.new_user, birth="1995-09-01")
        self.browser.get(self.live_server_url + '/account/login')


        username = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")
        submit = self.browser.find_element_by_name("confirm")

        username.send_keys("test_user")
        password.send_keys("azerty")
        submit.click()

    def tearDown(self):
        self.browser.quit()

    def test_publie_annonce(self):
        self.browser.get(self.live_server_url+'/create')
        # On enregistre les champs
        title_input = self.browser.find_element_by_name("title")
        annonce_input = self.browser.find_element_by_name("text")
        submit_input = self.browser.find_element_by_name("confirm")

        # On remplit les champs pour enregistrer une annonce
        title_input.send_keys("Test titre")
        annonce_input = annonce_input.send_keys("lorem ipsumlorem ipsumlorem ipsumlorem ipsum")

        # Clique sur le bouton de confirmation
        submit_input.click()

        self.browser.get(self.live_server_url)

        # puis on verifie
        self.assertIn("Test titre", self.browser.page_source)
