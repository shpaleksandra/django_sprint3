from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/about/', include('pages.urls'), namespace='pages'),
    path('pages/rules/', include('pages.urls'), namespace='pages'),
    path('', include('blog.urls'), namespace='blog'),
    path('posts/<int:id>/', include('blog.urls'), namespace='blog'),
    path('category/<slug:category_slug>/', include('blog.urls'), namespace='blog')
]
