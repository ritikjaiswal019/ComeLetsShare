from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="homePage"),
    path('AboutUs/', views.about, name="aboutUs"),
    path('Subscribe/', views.subscribe, name="subscribe"),
    path('Donate/', views.donate, name="donate"),
    path('Events/Past', views.pastEvent, name="pastEvents"),
    path('Events/Past/<int:event_id>', views.singleEvent, name="singleEvent"),
    path('Events/Upcoming', views.upcomingEvent, name="upcomingEvents"),
    path('ContactUs/', views.contact, name="contactUs"),
    path('ContactUs/query', views.submitQuery, name="submit-Query"),

]