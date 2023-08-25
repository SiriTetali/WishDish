from django.urls import path,include
from .views import Home
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib import admin
urlpatterns = [
    path('',Home.as_view(),name="home"),
    # path('admin/',admin.site.urls),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
