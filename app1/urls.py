from django.urls import path
from . import views
from .views import HomePageView, SearchResultsView

urlpatterns = [
    path("", views.HomePage, name="home"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("quizzes/", views.quiz, name="quizzes"),
    path("art1/", views.art1, name="art1"),
    path("art2/", views.art2, name="art2"),
]