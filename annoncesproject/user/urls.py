from django.conf.urls import url
from django.contrib.auth import views as auth_views
from user import views

urlpatterns = [
    url(r'^login/$', auth_views.login,  {'redirect_authenticated_user': True}, name="login"),
    url(r'^logout/$', auth_views.logout, name="logout"),
    url(r'^signup/$', views.CreateProfile, name="signup"),
    url(r'^profile/$', views.UpdateProfile, name="profile")


]