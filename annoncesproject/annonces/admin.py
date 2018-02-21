from django.contrib import admin
from annonces.models import Annonce, Image


class ImageInline(admin.TabularInline):
    model = Image

class AnnonceAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'date')
    list_filter = ('date', 'status')
    list_editable = ('status',)
    list_display_links = ('title', )
    ordering = ['-status']
    prepopulated_fields = {"slug_title": ("title",)}
    inlines = [ImageInline]



"""
    def test(self, obj):
        return "<a href='https://www.google.fr'>g</a>"
    test.allow_tags = True
    #permet de suivre un lien
 """
admin.site.register(Annonce, AnnonceAdmin)

admin.site.register(Image)
