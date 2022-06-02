from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path


urlpatterns=[
    path('',views.home,name='home'),
    path('login-user', views.login_user, name="login"),
    path('logout-user', views.logout_user, name="logout"),
    path('register-user', views.register_user, name="register"),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)