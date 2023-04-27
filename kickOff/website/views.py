from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
from .utils import  *


# About Players
class WebsiteHome(DataMixin, ListView):
    model = Players
    template_name = 'website/index.html'
    context_object_name = 'players'
    extra_context = {'title': 'Index Page'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Index page")
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Players.objects.filter(is_published=True).select_related('club')


class AddPlayer(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPlayerForm
    template_name = 'website/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Add player")
        return dict(list(context.items()) + list(c_def.items()))


class ShowPlayer(DataMixin, DetailView):
    model = Players
    template_name = 'website/player.html'
    slug_url_kwarg = 'player_slug'
    context_object_name = 'player'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Player")
        return dict(list(context.items()) + list(c_def.items()))

# About Club
class PlayersClub(DataMixin, ListView):
    model = Players
    template_name = 'website/index.html'
    context_object_name = 'players'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Club - ' + str(context['players'][0].club))
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Players.objects.filter(club__slug=self.kwargs['club_slug'], is_published=True).select_related('club')


# About Register and Login
class RegisterUser(DataMixin, CreateView):
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


class LoginUser(DataMixin, LoginView):
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


def about(request):
    return render(request, 'website/about.html', {'title': 'About Players'})


def football(request):
    return HttpResponse("About football")


def pagenotfound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')


def accessforbiden(request, exception):
    return HttpResponseNotFound('<h1>Access forbidden</h1>')


def servererror(request, exception):
    return HttpResponseNotFound('<h1>Error Server</h1>')


def error(request, exception):
    return HttpResponseNotFound('<h1>Error</h1>')
