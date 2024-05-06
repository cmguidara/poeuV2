from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate, PerfilUpdate




urlpatterns = [
    #sintaxe para adicionar novo path: path ('', view, name="")
    path('login/', auth_views.LoginView.as_view(
            template_name='usuarios/login.html'
         ), name="login"),

    path('logout/', auth_views.LogoutView.as_view(
            template_name='usuarios/logout_form.html'
        ), name="logout"),


    path('registrar/', UsuarioCreate.as_view(), name='registrar'),

    path('perfil/', PerfilUpdate.as_view(), name='perfil'),






]

