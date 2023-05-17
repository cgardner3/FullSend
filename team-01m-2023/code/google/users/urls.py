from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
	path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
	path("", views.home,name="home"),
	path("main/", views.main,name="main"),
	path("discovery/", views.discovery,name="discovery"),
	path("matches/", views.matches,name="matches"),
	path("message/", views.message, name="message"),
	path("settings/", views.settings, name="settings"),
	path("thanks/", views.thanks, name="thanks"),
	path("signup/", views.signup, name="signup"),
	path("logout/", views.logout_view,name="logout"),
]