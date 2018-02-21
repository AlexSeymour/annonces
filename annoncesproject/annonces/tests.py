from django.test import TestCase
from django.contrib.auth.models import User
from annonces.models import Annonce
from user.models import Profile
from django.test import Client


class AnnonceTestCase(TestCase):

    def test_home_page_displays_all_list_items(self):

        # Création d' un utilisateur
        new_user = User.objects.create_user(username="test_user", email="test@gmail.com", password="azerty")
        profile = Profile.objects.create(user=new_user, birth="1995-09-01")

        annonce = Annonce.objects.create(user=profile, title="Test 1", text="Text")
        c = Client()
        response = c.get("/")

        self.assertContains(response, "Test 1")  # On regarde si l' annonce apparait dans le code source

