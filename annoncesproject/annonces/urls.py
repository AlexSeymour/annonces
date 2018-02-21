from django.conf.urls import url
from annonces import views
urlpatterns = [
    url(r'^$', views.AnnonceList, name="list"),
    url(r'^mes-annonces/$', views.user_annonce_list, name="user-list"),
    url(r'^(?P<page>[\d]+)$', views.AnnonceList, name="list-page"),
    url(r'^mes-annonces/(?P<page>[\d]+)$', views.user_annonce_list, name="user-list-page"),
    url(r'^user-list$', views.user_annonce_list, name="user-list"),
    url(r'^create$', views.create_annonce, name="create"),
    url(r'update/(?P<pk>[\d]+)$', views.update, name="update"),
    url(r'^delete/(?P<slug>[-\w]+)$', views.AnnonceDelete.as_view(), name="delete"),
    # url(r'^(?P<slug>[-\w]+)/$', views.AnnonceDetail.as_view(), name="detail"),
    url(r'^(?P<slug>[-\w]+)/$', views.annonce_detail, name="detail"),
]