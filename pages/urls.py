from django.urls import path
from .views import HomePageView, Profile, contactView, successView, About, Drone

urlpatterns = [
path('', HomePageView.as_view(), name='home'),
path('profile/',Profile.as_view(), name='profile'),
path('contact/', contactView, name='contact'),
path('success/', successView, name='success'),
path('about/', About.as_view(), name='about' ),
path('drone/',Drone.as_view(), name='drone' ),



]