from django.contrib import admin
from myapp import models
# Register your models here.
class TopicView(admin.ModelAdmin):
    list_display=('Topic_name',)
    search_fields=('Topic_name',)
class WebpageView(admin.ModelAdmin):
    list_display=('topic','name','url')
    search_fields=('topic','name')
    list_editable=('name',)
    list_filter=('topic',)
class AccessView(admin.ModelAdmin):
    list_display=('webpage','datetime')
    search_fields=('webpage','datetime')

admin.site.register(models.Topic,TopicView)
admin.site.register(models.Webpage,WebpageView)
admin.site.register(models.AccessDetails,AccessView)
admin.site.register(models.ProfilePic)