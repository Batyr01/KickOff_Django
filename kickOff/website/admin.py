from django.contrib import admin

from .models import *


class PlayersAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullName', 'about', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'fullName')
    search_fields = ('fullName', 'club', 'about')
    prepopulated_fields = {"slug": ("fullName",)}


class ClubAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Players, PlayersAdmin)
admin.site.register(Club, ClubAdmin)
