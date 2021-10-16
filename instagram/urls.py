from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('' , views.post, name='post'),
    path('profile/' , views.profile, name='profile'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)