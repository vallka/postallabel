from django.urls import path

from .views import HomePageView, AboutPageView, ServicesPageView, MainPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('services/', ServicesPageView.as_view(), name='services'),
    path('main/', MainPageView.as_view(), name='main'),
]
