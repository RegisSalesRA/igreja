from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Jovens, Ministerio


# Register your models here.

@admin.register(Jovens)
class JovensAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ministerio', 'igreja', 'celula']


@admin.register(Ministerio)
class MinisterioAdmin(admin.ModelAdmin):
    list_display = ['ministerio']