from django.contrib import admin

# Register your models here.
from igreja.models import Celula, Igreja, Lideres, Ministerio


admin.site.register(Igreja)
admin.site.register(Celula)
admin.site.register(Lideres)
admin.site.register(Ministerio)