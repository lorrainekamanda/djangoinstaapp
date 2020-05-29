from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url('^$', views.register, name = 'blog-register'),
    url('^home$', views.home, name = 'blog-home'),
    url('^about/$', views.about, name = 'blog-about')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)