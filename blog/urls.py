from django.conf.urls import url
from . import views
from .views import ImageView,ImageDetail,CreateDetail,UpdateDetail,CreateComment,CommentView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .models import Image
from django.urls import path
urlpatterns = [ 
     path('image/<int:imageid>/preference/<int:userpreference>', views.imagepreference, name='imagepreference'),
    path('', ImageView.as_view(), name = 'blog-home'),
    path('image/<int:pk>/', ImageDetail.as_view(), name = 'image-detail'),
    path('image/<int:pk>/comment', CreateComment.as_view(), name = 'comment-detail'),
    path('image/<int:pk>/update', UpdateDetail.as_view(), name = 'image-update'),
    path('image/new/', CreateDetail.as_view(), name = 'image-create'),
    path('register/', views.register, name = 'blog-register'),
    path('profile/', views.profile, name = 'blog-profile'),
    path('login', auth_views.LoginView.as_view(template_name = 'blog/login.html'), name = 'blog-login'),
    path('logout', auth_views.LogoutView.as_view(template_name = 'blog/logout.html'), name = 'blog-logout'),
    path('search/', views.search_results, name='search_results'),
    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)