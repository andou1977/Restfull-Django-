from django.contrib import admin

# Register your models here.
from Api.models import Institution, Faculter, Option, Expert, Utilisateur

admin.site.register(Institution)
admin.site.register(Faculter)
admin.site.register(Option)
admin.site.register(Expert)
admin.site.register(Utilisateur)
