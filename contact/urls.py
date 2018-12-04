from django.urls import path

from . import views


urlpatterns = [
    path('contact', views.ContactView.as_view(), name='contact'),
    path('thanks', views.ThanksView.as_view(), name='thanks'),
    path('about', views.AboutView.as_view(), name='about'),
]
