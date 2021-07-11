from django.contrib import admin
from .models import Post
from .models import Contact

# Register your models here.
admin.site.register(Contact)



@admin.register(Post)
class PostModelAdimi(admin.ModelAdmin):
  list_display = ['id','title','desc']


