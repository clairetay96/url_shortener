
from django.urls import path
from .views import UrlView, CreateUrlView, redirect_view

urlpatterns = [
		path('', CreateUrlView.as_view()),
    path('list-urls', UrlView.as_view()),
    path('<str:code>', redirect_view),
]