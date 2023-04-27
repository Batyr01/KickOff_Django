from website.models import *


class DataMixin:
    paginate_by = 2
    def get_user_context(self, **kwargs):
        context = kwargs
        clubs = Club.objects.all()
        context['clubs'] = clubs
        return context