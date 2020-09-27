from django.contrib import admin

# Register your models here.
from mainapp.models import GameTypes, Game

admin.site.register(GameTypes)
admin.site.register(Game)

#class NewAdmin(admin.ModelAdmin):
 #   pass


#admin.site.register(Author, AuthorAdmin)
