from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Location
from .models import Post

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Post)
