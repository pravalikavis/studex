"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.cards, name='cards'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),

url(r'^post/sort/(?P<q>\d+)/$',views.post_sort,name='post_sort'),
    url(r'^cards.html$', views.cards, name='cards'),

url(r'^signup.html$', views.register, name='signup'),

url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),

url(r'^logout/', views.logout_view, name='logout_view'),
    url(r'^accounts/profile', views.cards, name='post_list'),
url(r'^upload.html$', views.upload, name='upload'),
url(r'^homepage.html$', views.homepage, name='homepage'),
url(r'^aboutus.html$', views.aboutus, name='aboutus'),
]
