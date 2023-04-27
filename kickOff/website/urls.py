from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    # Players
    path('player/<slug:player_slug>/', ShowPlayer.as_view(), name='player'),
    path('addpage/', AddPlayer.as_view(), name='add_page'),
    path('<slug:club_slug>/players/', PlayersClub.as_view(), name='club_players'),
    path('players/', ShowPlayers.as_view(), name='players'),

    # Clubs
    path('clubs/', ShowClubs.as_view(), name='clubs'),
    path('club/<slug:club_slug>/', ShowClub.as_view(), name='club'),
    path('<slug:league_slug>/clubs/', LeagueClubs.as_view(), name='league_clubs'),

    # Leagues
    path('leagues/', ShowLeagues.as_view(), name='leagues'),
    path('league/<slug:league_slug>/', ShowLeague.as_view(), name='league'),

    path('', home, name='home'),
    path('contact/', ContactFormView.as_view(), name='contact'),

    # Register Login Logout
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),

]

