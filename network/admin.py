from csv import list_dialects
from django.contrib import admin

# Register your models here.
from network.models import PostInfo,PostLike

class PostInfoAdmin(admin.ModelAdmin):
    list_display=("id","spostuser","spostinfo","sposttime")


admin.site.register(PostInfo,PostInfoAdmin)
admin.site.register(PostLike)

