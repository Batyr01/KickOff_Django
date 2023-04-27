from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('player/<slug:player_slug>/', ShowPlayer.as_view(), name='player'),
    path('addpage/', AddPlayer.as_view(), name='add_page'),
    path('club/<slug:club_slug>/', PlayersClub.as_view(), name='club'),
    path('', WebsiteHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('football/', football, name='aboutFootball'),

    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),

]

