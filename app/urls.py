from django.urls import path
from  .views import *

urlpatterns = [
    path("login/", login_view, name="login"),
    path("cadastro/", cadastro_view, name="cadastro"),
    path("logout/", logout_view, name="logout"),
    path("", home_view, name="home"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("registro_humor/", registro_humor_view, name="registro_humor"),
    path("profissionais/", profissionais_view, name='profissionais_view'),
]