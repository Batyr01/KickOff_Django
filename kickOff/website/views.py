from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .forms import *
from .permissions import IsAdminOrReadOnly
from .serializer import PlayersSerializer
from .utils import  *


def home(request):
    return render(request, 'website/index.html', {'title': 'Index Page'})


# About Api ------------------------------------------------------------------------------------------------------------

# class PlayersViewSet(viewsets.ModelViewSet):
#     queryset = Players.objects.all()
#     serializer_class = PlayersSerializer
class PlayersAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000

class PlayersAPIView(generics.ListCreateAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
    permission_classes = (IsAdminOrReadOnly, )
    pagination_class = PlayersAPIListPagination

# class PlayersAPIUpdate(generics.UpdateAPIView):
#     queryset = Players.objects.all()
#     serializer_class = PlayersSerializer


class PlayersAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
    permission_classes = (IsAdminOrReadOnly,)

# About Api ------------------------------------------------------------------------------------------------------------


# About Players --------------------------------------------------------------------------------------------------------
class ShowPlayers(PlayersMixin, ListView):
    model = Players
    template_name = 'website/players.html'
    context_object_name = 'players'
    extra_context = {'title': 'Players Page'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Players page")
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Players.objects.filter(is_published=True).select_related('club')


class AddPlayer(LoginRequiredMixin, PlayersMixin, CreateView):
    form_class = AddPlayerForm
    template_name = 'website/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Add player")
        return dict(list(context.items()) + list(c_def.items()))


class ShowPlayer(PlayersMixin, DetailView):
    model = Players
    template_name = 'website/player.html'
    slug_url_kwarg = 'player_slug'
    context_object_name = 'player'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Player")
        return dict(list(context.items()) + list(c_def.items()))


class PlayersClub(PlayersMixin, ListView):
    model = Players
    template_name = 'website/players.html'
    context_object_name = 'players'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Club')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Players.objects.filter(club__slug=self.kwargs['club_slug'], is_published=True).select_related('club')


# About Players --------------------------------------------------------------------------------------------------------




# About Clubs --------------------------------------------------------------------------------------------------------
class ShowClubs(ClubMixin, ListView):
    model = Club
    template_name = 'website/clubs.html'
    context_object_name = 'clubs'
    extra_context = {'title': 'Clubs Page'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Index page")
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Club.objects.filter(is_published=True)


class ShowClub(ClubMixin, DetailView):
    model = Club
    template_name = 'website/club.html'
    slug_url_kwarg = 'club_slug'
    context_object_name = 'club'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Club")
        return dict(list(context.items()) + list(c_def.items()))


class LeagueClubs(ClubMixin, ListView):
    model = Club
    template_name = 'website/clubs.html'
    context_object_name = 'clubs'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        league = League.objects.get(slug=self.kwargs['league_slug'])
        clubs = Club.objects.filter(league_id = league.id)
        c_def = self.get_user_context(title='League', clubs = clubs)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Club.objects.filter(league__slug=self.kwargs['league_slug'], is_published=True)
# About Clubs --------------------------------------------------------------------------------------------------------



# About Leagues --------------------------------------------------------------------------------------------------------
class ShowLeagues(LeagueMixin, ListView):
    model = League
    template_name = 'website/leagues.html'
    context_object_name = 'leagues'
    extra_context = {'title': 'Leagues Page'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Index page")
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return League.objects.filter(is_published=True)


class ShowLeague(LeagueMixin, DetailView):
    model = League
    template_name = 'website/league.html'
    slug_url_kwarg = 'league_slug'
    context_object_name = 'league'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="League")
        return dict(list(context.items()) + list(c_def.items()))
# About Leagues --------------------------------------------------------------------------------------------------------





# About Register and Login ---------------------------------------------------------------------------------------------
class RegisterUser(PlayersMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'website/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Register')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(PlayersMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'website/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Login')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
# About Register and Login ---------------------------------------------------------------------------------------------





# Others ---------------------------------------------------------------------------------------------
class ContactFormView(PlayersMixin, FormView):
    form_class = ContactForm
    template_name = 'website/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='FeedBAck')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')



def pagenotfound(request, exception):
    return render(request, 'website/error.html', {'error': 'Page Not Found'})


def accessforbiden(request, exception):
    # return HttpResponseNotFound('<h1>Access forbidden</h1>')
    return render(request, 'website/error.html', {'error': 'Access Forbidden'})


# def servererror(request, exception):
#     # return HttpResponseNotFound('<h1>Error Server</h1>')
#     return render(request, 'website/error.html')

def servererror(request, *args, **argv):
    return render(request, 'website/error.html', {'error': 'Server Error'},status=500)

def error(request, exception):
    # return HttpResponseNotFound('<h1>Error</h1>')
    return render(request, 'website/error.html', {'error': 'Error'})
