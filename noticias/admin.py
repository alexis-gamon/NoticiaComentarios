from django.contrib import admin
from .models import Noticias, Comentario

#class ComentarioInline(admin.StackedInline):
#    model = Comentario

class ComentarioInline(admin.TabularInline):
    model = Comentario

class NoticiaAdmin(admin.ModelAdmin):
    inlines = [
        ComentarioInline
    ]
        

admin.site.register(Noticias, NoticiaAdmin)
admin.site.register(Comentario)