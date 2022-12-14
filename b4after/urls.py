from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("users.urls")),
    path('books/', include("books.urls")),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
