from website.models import *


class PlayersMixin:
    paginate_by = 5
    def get_user_context(self, **kwargs):
        context = kwargs
        clubs = Club.objects.all()
        context['clubs'] = clubs
        return context


class ClubMixin:
    paginate_by = 8
    def get_user_context(self, **kwargs):
        context = kwargs
        # clubs = Club.objects.all()
        # context['clubs'] = clubs
        return context


class LeagueMixin:
    paginate_by = 8
    def get_user_context(self, **kwargs):
        context = kwargs
        leagues = League.objects.all()
        context['leagues'] = leagues
        return context