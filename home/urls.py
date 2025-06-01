from django.urls import path
from .views import HomePageView, AboutPageView, ServicePageView, ThankYouView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='About'),
    path('service', ServicePageView.as_view(), name='Service'),
    path('thankyou', ThankYouView.as_view(), name='thank_you')
]