from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class PlayersAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullName', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'fullName')
    search_fields = ('fullName', 'club', 'about')
    prepopulated_fields = {"slug": ("fullName",)}
    fields = ('fullName', 'slug','photo', 'about', 'club','get_html_photo','time_create', 'time_update', 'is_published')
    readonly_fields = ('get_html_photo','time_create', 'time_update')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Изображение"


class ClubAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create', 'get_html_photo',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    fields = (
        'name', 'slug', 'logo', 'about', 'league', 'get_html_photo', 'time_create', 'time_update', 'is_published')
    readonly_fields = ('get_html_photo', 'time_create', 'time_update')

    def get_html_photo(self, object):
        if object.logo:
            return mark_safe(f"<img src='{object.logo.url}' width=50>")

    get_html_photo.short_description = "Изображение"

class LeagueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create', 'get_html_photo',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    fields = (
    'name', 'slug', 'logo', 'about', 'get_html_photo', 'time_create', 'time_update', 'is_published')
    readonly_fields = ('get_html_photo', 'time_create', 'time_update')


    def get_html_photo(self, object):
        if object.logo:
            return mark_safe(f"<img src='{object.logo.url}' width=50>")

    get_html_photo.short_description = "Изображение"

admin.site.register(Players, PlayersAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(League, LeagueAdmin)

admin.site.site_title='KickOff'
admin.site.site_header='Админ Панель Сайта KickOff'
