from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog import views
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginpage, name='login'),
    path('logout/', logoutpage, name='logout'),
    path('register/', register, name='register'),
    path('home/', home,name='home'),
    path('add/',addBlog,name='addblog'),
    path('like/<str:pk>',likeBlog,name='like'),
    path('delete/<int:id>',delBlog,name='delete'),
    path('update/<str:pk>/',Blogupdate, name="update")
]+ static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
