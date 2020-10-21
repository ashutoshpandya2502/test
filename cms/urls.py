from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cms/home/',views.index,name="home"),
    path('cms/about_us/',views.about_us,name="about_us"),
    path('cms/sign_up/',views.signup,name="signup"),
    path('cms/login/',views.login_user,name="login"),
    path('cms/show_client_edit/<int:agent_id>/',views.show_client_edit,name="show_client_edit"),
    path('cms/add_client/<int:agent_id>/',views.add_client,name="add_client"),


]